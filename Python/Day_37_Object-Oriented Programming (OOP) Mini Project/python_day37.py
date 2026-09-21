# =====================================================================
# Day 37 — Object-Oriented Programming (OOP) Mini Project
# Script: oop_mini_project.py
# System: Machine Learning Experiment & Model Registry
# =====================================================================

from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
import json
import os


# =====================================================================
# 1. ABSTRACT BASE CLASS (ESTIMATOR INTERFACE)
# =====================================================================

class BaseModel(ABC):
    """Abstract Base Class enforcing standard estimator API contracts."""

    def __init__(self, model_name: str):
        self.model_name = model_name
        self._is_fitted = False

    @property
    def is_fitted(self) -> bool:
        return self._is_fitted

    @abstractmethod
    def fit(self, X: list[list[float]], y: list[int]):
        """Fit model to training feature matrix X and target vector y."""
        pass

    @abstractmethod
    def predict(self, X: list[list[float]]) -> list[int]:
        """Generate predictions for feature matrix X."""
        pass

    def evaluate(self, X: list[list[float]], y: list[int]) -> dict[str, float]:
        """Polymorphic evaluation routine computing classification accuracy."""
        if not self._is_fitted:
            raise RuntimeError(f"Cannot evaluate unfitted model: {self.model_name}")

        predictions = self.predict(X)
        if len(predictions) != len(y):
            raise ValueError("Dimensions of predictions and targets do not match.")

        correct_count = sum(1 for pred, actual in zip(predictions, y) if pred == actual)
        accuracy = round(correct_count / len(y), 4) if y else 0.0

        return {"accuracy": accuracy}


# =====================================================================
# 2. CONCRETE ESTIMATOR IMPLEMENTATIONS (POLYMORPHISM)
# =====================================================================

class MajorityClassifier(BaseModel):
    """Baseline estimator predicting the statistical mode of training targets."""

    def __init__(self):
        super().__init__(model_name="MajorityClassifier")
        self.majority_class_ = None

    def fit(self, X: list[list[float]], y: list[int]):
        if not y:
            raise ValueError("Target collection y cannot be empty.")

        counts = {}
        for label in y:
            counts[label] = counts.get(label, 0) + 1

        self.majority_class_ = max(counts, key=counts.get)
        self._is_fitted = True
        return self

    def predict(self, X: list[list[float]]) -> list[int]:
        if not self._is_fitted:
            raise RuntimeError("Estimator not fitted yet.")
        return [self.majority_class_ for _ in X]


class ThresholdClassifier(BaseModel):
    """Rule-based estimator making predictions by splitting on a single feature."""

    def __init__(self, feature_index: int = 0, threshold: float = 0.5):
        super().__init__(model_name="ThresholdClassifier")
        self.feature_index = feature_index
        self.threshold = threshold

    def fit(self, X: list[list[float]], y: list[int]):
        # Stateless rule baseline: verify feature presence
        if not X or self.feature_index >= len(X[0]):
            raise IndexError(f"Feature index {self.feature_index} is out of bounds for input X.")
        self._is_fitted = True
        return self

    def predict(self, X: list[list[float]]) -> list[int]:
        if not self._is_fitted:
            raise RuntimeError("Estimator not fitted yet.")
        return [1 if row[self.feature_index] >= self.threshold else 0 for row in X]


# =====================================================================
# 3. EXPERIMENT RECORD CLASS (ENCAPSULATION & OPERATOR OVERLOADING)
# =====================================================================

class ExperimentRun:
    """Encapsulates execution parameters, evaluation metrics, and metadata."""

    def __init__(self, run_id: str, model_name: str, hyperparams: dict, metrics: dict, timestamp: str = None):
        self._run_id = run_id
        self.model_name = model_name
        self.hyperparams = dict(hyperparams)
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.metrics = metrics  # Triggers property setter validation

    @property
    def run_id(self) -> str:
        return self._run_id

    @property
    def metrics(self) -> dict[str, float]:
        return self._metrics

    @metrics.setter
    def metrics(self, metric_dict: dict[str, float]):
        if not isinstance(metric_dict, dict) or "accuracy" not in metric_dict:
            raise ValueError("Metrics must be a dictionary containing at least an 'accuracy' key.")
        acc = metric_dict["accuracy"]
        if not (0.0 <= acc <= 1.0):
            raise ValueError(f"Accuracy must be strictly bounded within [0.0, 1.0]. Given: {acc}")
        self._metrics = {k: round(float(v), 4) for k, v in metric_dict.items()}

    # --- Operator Overloading ---
    def __lt__(self, other) -> bool:
        """Enables native sorting based on accuracy."""
        if not isinstance(other, ExperimentRun):
            return NotImplemented
        return self.metrics["accuracy"] < other.metrics["accuracy"]

    def __eq__(self, other) -> bool:
        if not isinstance(other, ExperimentRun):
            return False
        return self.run_id == other.run_id and self.metrics == other.metrics

    def __repr__(self) -> str:
        return (f"ExperimentRun(id='{self.run_id}', model='{self.model_name}', "
                f"acc={self.metrics['accuracy']:.2%}, ts='{self.timestamp}')")

    # --- Serialization Factories ---
    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "model_name": self.model_name,
            "hyperparams": self.hyperparams,
            "metrics": self.metrics,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            run_id=data["run_id"],
            model_name=data["model_name"],
            hyperparams=data["hyperparams"],
            metrics=data["metrics"],
            timestamp=data["timestamp"]
        )


# =====================================================================
# 4. REGISTRY MANAGER CLASS (COLLECTION CONTROLLER & PERSISTENCE)
# =====================================================================

class ModelRegistry:
    """Manages experiment runs, queries leaderboard standings, and handles disk I/O."""

    def __init__(self, registry_name: str = "Production_Registry"):
        self.registry_name = registry_name
        self._runs: list[ExperimentRun] = []

    def register_run(self, run: ExperimentRun):
        if not isinstance(run, ExperimentRun):
            raise TypeError("Only instances of ExperimentRun can be registered.")
        if any(existing.run_id == run.run_id for existing in self._runs):
            raise ValueError(f"Run ID '{run.run_id}' already exists in registry.")
        self._runs.append(run)

    def get_best_run(self) -> ExperimentRun | None:
        if not self._runs:
            return None
        # Uses overloaded __lt__ internally
        return max(self._runs)

    def get_leaderboard(self) -> list[ExperimentRun]:
        # Sorts descending by accuracy
        return sorted(self._runs, reverse=True)

    def filter_by_model(self, model_name: str) -> list[ExperimentRun]:
        return [r for r in self._runs if r.model_name.lower() == model_name.lower()]

    def save_to_disk(self, filepath: str | Path):
        path = Path(filepath)
        payload = {
            "registry_name": self.registry_name,
            "exported_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_runs": len(self._runs),
            "runs": [r.to_dict() for r in self._runs]
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

    @classmethod
    def load_from_disk(cls, filepath: str | Path):
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Registry storage file not found at: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        registry_instance = cls(registry_name=data.get("registry_name", "Loaded_Registry"))
        for run_dict in data.get("runs", []):
            run_obj = ExperimentRun.from_dict(run_dict)
            registry_instance.register_run(run_obj)

        return registry_instance

    def __len__(self) -> int:
        return len(self._runs)


# =====================================================================
# 5. PIPELINE EXECUTION & INTEGRATION TEST SUITE
# =====================================================================

if __name__ == "__main__":
    print("=" * 65)
    print("DAY 37 OOP MINI PROJECT: EXPERIMENT & REGISTRY SYSTEM")
    print("=" * 65)

    # -------------------------------------------------------------
    # Step A: Synthetic Data Preparation
    # -------------------------------------------------------------
    X_train = [[1.2, 0.5], [0.3, 0.8], [2.1, 1.5], [0.1, 0.2], [1.8, 2.0], [0.4, 0.6]]
    y_train = [1,           0,           1,           0,           1,           0]

    X_test  = [[1.5, 0.9], [0.2, 0.4], [2.4, 1.2], [0.5, 0.7]]
    y_test  = [1,           0,           1,           1]

    # -------------------------------------------------------------
    # Step B: Abstract Class Guard Verification
    # -------------------------------------------------------------
    try:
        abstract_instance = BaseModel("InvalidDirectInstance")
    except TypeError as err:
        print(f"\n[ABC Guard Passed] Abstract instantiation blocked:\n  -> {err}")

    # -------------------------------------------------------------
    # Step C: Polymorphic Model Training & Evaluation
    # -------------------------------------------------------------
    models: list[BaseModel] = [
        MajorityClassifier(),
        ThresholdClassifier(feature_index=0, threshold=1.0),
        ThresholdClassifier(feature_index=1, threshold=0.7)
    ]

    registry = ModelRegistry("Alpha_Model_Registry")

    print("\n--- Training & Registering Runs ---")
    for idx, model in enumerate(models, start=1):
        model.fit(X_train, y_train)
        metrics = model.evaluate(X_test, y_test)

        params = {}
        if isinstance(model, ThresholdClassifier):
            params = {"feature_index": model.feature_index, "threshold": model.threshold}

        run_record = ExperimentRun(
            run_id=f"RUN-00{idx}",
            model_name=model.model_name,
            hyperparams=params,
            metrics=metrics
        )
        registry.register_run(run_record)
        print(f"  Registered: {run_record}")

    # -------------------------------------------------------------
    # Step D: Operator Overloading & Leaderboard Sorting
    # -------------------------------------------------------------
    print("\n--- Leaderboard Ranking (Sorted using Overloaded __lt__) ---")
    leaderboard = registry.get_leaderboard()
    for rank, entry in enumerate(leaderboard, start=1):
        print(f"  Rank {rank}: [{entry.run_id}] {entry.model_name:<20} | Accuracy: {entry.metrics['accuracy']:.2%}")

    best_run = registry.get_best_run()
    print(f"\nTop Champion Model: {best_run.run_id} ({best_run.model_name}) with {best_run.metrics['accuracy']:.2%}")

    # -------------------------------------------------------------
    # Step E: File Persistence (JSON Serialization Round-Trip)
    # -------------------------------------------------------------
    persistence_file = Path("registry.json")
    print(f"\n--- Persisting Registry to Disk: {persistence_file.name} ---")
    registry.save_to_disk(persistence_file)
    print(f"  Successfully wrote {len(registry)} records.")

    print("\n--- Reloading Registry into a Fresh Instance ---")
    reloaded_registry = ModelRegistry.load_from_disk(persistence_file)
    print(f"  Reloaded Registry Name: {reloaded_registry.registry_name}")
    print(f"  Total Runs Recovered:   {len(reloaded_registry)}")
    print(f"  Champion Preserved:     {reloaded_registry.get_best_run().run_id} "
          f"({reloaded_registry.get_best_run().metrics['accuracy']:.2%})")

    assert len(registry) == len(reloaded_registry), "Registry lengths do not match!"
    assert registry.get_best_run() == reloaded_registry.get_best_run(), "Champion runs do not match!"
    print("\n[SUCCESS] Day 37 OOP Mini Project completed and verified.")

    # Cleanup temporary storage file
    if persistence_file.exists():
        os.remove(persistence_file)
        print("  Cleaned up temporary registry.json artifact.")





        