# ==========================================
# Day 36 — Python Polymorphism
# Script: polymorphism.py
# ==========================================

from abc import ABC, abstractmethod
import math

print("=== 1. DUCK TYPING & INTERCHANGEABLE APIS ===")
class CSVLoader:
    def load(self, source):
        return f"[CSVLoader] Loaded tabular rows from '{source}'"

class ParquetLoader:
    def load(self, source):
        return f"[ParquetLoader] Loaded columnar data from '{source}'"

class SQLLoader:
    def load(self, source):
        return f"[SQLLoader] Executed query and read tables from '{source}'"

def run_data_ingestion(loader, source):
    """Duck-typed pipeline step: cares only that loader has a .load() method."""
    return loader.load(source)

loaders = [
    (CSVLoader(), "s3://bucket/users.csv"),
    (ParquetLoader(), "s3://bucket/events.parquet"),
    (SQLLoader(), "SELECT * FROM transactions;")
]

for ldr, path in loaders:
    print(run_data_ingestion(ldr, path))


print("\n=== 2. ABSTRACT BASE CLASSES (ABC) ===")
class BaseDataTransformer(ABC):
    @abstractmethod
    def fit_transform(self, data):
        """Subclasses must provide concrete implementation."""
        pass

class LogScaler(BaseDataTransformer):
    def fit_transform(self, data):
        return [round(math.log(x), 4) for x in data if x > 0]

class IdentityScaler(BaseDataTransformer):
    def fit_transform(self, data):
        return list(data)

# Verifying abstract enforcement:
# BaseDataTransformer() -> Raises TypeError

scalers = [LogScaler(), IdentityScaler()]
sample_nums = [1, 10, 100]

for s in scalers:
    print(f"{type(s).__name__}: {s.fit_transform(sample_nums)}")


print("\n=== 3. OPERATOR OVERLOADING (DUNDER METHODS) ===")
class MetricVector:
    def __init__(self, accuracy, f1):
        self.accuracy = accuracy
        self.f1 = f1

    def __add__(self, other):
        if not isinstance(other, MetricVector):
            raise TypeError("Operands must be MetricVector instances")
        return MetricVector(
            round((self.accuracy + other.accuracy) / 2, 4),
            round((self.f1 + other.f1) / 2, 4)
        )

    def __eq__(self, other):
        if not isinstance(other, MetricVector):
            return False
        return self.accuracy == other.accuracy and self.f1 == other.f1

    def __repr__(self):
        return f"MetricVector(acc={self.accuracy}, f1={self.f1})"

v1 = MetricVector(0.92, 0.90)
v2 = MetricVector(0.96, 0.94)
v3 = MetricVector(0.92, 0.90)

print("v1 + v2 (Averaged Metrics):", v1 + v2)
print("v1 == v3:", v1 == v3)
print("v1 == v2:", v1 == v2)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Basic Method Overriding Polymorphism
class AudioFile:
    def play(self):
        return "Playing generic audio"

class MP3File(AudioFile):
    def play(self):
        return "Streaming compressed MP3 audio stream"

class WavFile(AudioFile):
    def play(self):
        return "Streaming uncompressed high-fidelity WAV audio"

audio_tracks = [MP3File(), WavFile()]
print("Q1 Audio playback:")
for track in audio_tracks:
    print("  ", track.play())


# Q2 — Polymorphic Function Iterator
class Circle:
    def draw(self):
        return "Drawing Circle (o)"

class Square:
    def draw(self):
        return "Drawing Square ([])"

class Triangle:
    def draw(self):
        return "Drawing Triangle (/\\)"

def render_shapes(shape_list):
    return [shape.draw() for shape in shape_list]

print("Q2 Shapes rendered:", render_shapes([Circle(), Square(), Triangle()]))


# Q3 — Duck Typing in Action
class JSONExporter:
    def export(self, payload):
        return f'{{"exported_json": "{payload}"}}'

class PlainTextExporter:
    def export(self, payload):
        return f"TXT >>> {payload}"

def serialize_data(exporter, payload):
    return exporter.export(payload)

print("Q3 JSON:", serialize_data(JSONExporter(), "model_weights_v1"))
print("Q3 Text:", serialize_data(PlainTextExporter(), "model_weights_v1"))


# Q4 — Operator Overloading (__add__)
class DatasetBatch:
    def __init__(self, records):
        self.records = list(records)

    def __add__(self, other):
        if not isinstance(other, DatasetBatch):
            raise TypeError("Can only add DatasetBatch to DatasetBatch")
        return DatasetBatch(self.records + other.records)

    def __repr__(self):
        return f"DatasetBatch(size={len(self.records)}, records={self.records})"

b1 = DatasetBatch([10, 20])
b2 = DatasetBatch([30, 40, 50])
merged_batch = b1 + b2
print("Q4 Merged Batch:", merged_batch)


# Q5 — Equality Comparison (__eq__)
class ModelCheckpoint:
    def __init__(self, epoch, val_loss):
        self.epoch = epoch
        self.val_loss = val_loss

    def __eq__(self, other):
        if not isinstance(other, ModelCheckpoint):
            return False
        return self.epoch == other.epoch and math.isclose(self.val_loss, other.val_loss, rel_tol=1e-5)

chk1 = ModelCheckpoint(10, 0.24501)
chk2 = ModelCheckpoint(10, 0.24501)
chk3 = ModelCheckpoint(11, 0.21000)
print(f"Q5 chk1 == chk2: {chk1 == chk2} | chk1 == chk3: {chk1 == chk3}")


# Q6 — Length Dunder (__len__)
class FeatureStore:
    def __init__(self):
        self._store = {}

    def register_feature(self, name, vector):
        self._store[name] = vector

    def __len__(self):
        return len(self._store)

fs = FeatureStore()
fs.register_feature("age", [25, 30, 45])
fs.register_feature("income", [50000, 70000, 120000])
fs.register_feature("credit_score", [720, 680, 810])
print(f"Q6 Total Features in Store: {len(fs)}")


# Q7 — Abstract Base Class Validator
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

class PostgresConnector(DatabaseConnector):
    def connect(self):
        return "Connected to PostgreSQL database at port 5432"

pg = PostgresConnector()
print("Q7 Database Contract:", pg.connect())


# Q8 — Custom String Representation Polymorphism
class AccuracyMetric:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f"Metric: Accuracy  | Value: {self.val:.2%}"

class LossMetric:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f"Metric: Log-Loss  | Value: {self.val:.4f}"

metric_reports = [AccuracyMetric(0.932), LossMetric(0.1852)]
print("Q8 Polymorphic Metric Outputs:")
for m in metric_reports:
    print("  ", m)


# Q9 — Comparison Operator Overloading (__lt__)
class CandidateModel:
    def __init__(self, name, val_acc):
        self.name = name
        self.val_acc = val_acc

    def __lt__(self, other):
        # Enables direct sorting by accuracy ascending
        return self.val_acc < other.val_acc

    def __repr__(self):
        return f"{self.name}(acc={self.val_acc})"

candidates = [
    CandidateModel("LogReg", 0.81),
    CandidateModel("XGBoost", 0.94),
    CandidateModel("RandomForest", 0.89)
]

print("Q9 Sorted Models (via __lt__):", sorted(candidates))


# Q10 — Challenge 🔥 (Interchangeable Estimator Evaluation Suite)
class BaseEstimatorStub(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

class MajorityClassEstimator(BaseEstimatorStub):
    def __init__(self):
        self.majority_class_ = None

    def fit(self, X, y):
        counts = {}
        for label in y:
            counts[label] = counts.get(label, 0) + 1
        self.majority_class_ = max(counts, key=counts.get)
        return self

    def predict(self, X):
        return [self.majority_class_] * len(X)

class ThresholdClassifier(BaseEstimatorStub):
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def fit(self, X, y):
        # Stateless fitting for baseline
        return self

    def predict(self, X):
        # Predict 1 if first feature > threshold else 0
        return [1 if row[0] > self.threshold else 0 for row in X]

def evaluate_estimators(estimators_map, X_test, y_test):
    """Polymorphically runs evaluation across any compliant estimator."""
    leaderboard = {}
    for name, model in estimators_map.items():
        preds = model.predict(X_test)
        correct = sum(1 for p, actual in zip(preds, y_test) if p == actual)
        acc = round(correct / len(y_test), 4) if y_test else 0.0
        leaderboard[name] = acc
    return leaderboard

# Synthetic test data
X_test_data = [[0.8, 1.2], [0.2, 0.4], [0.9, 0.1], [0.1, 0.9]]
y_test_data = [1, 0, 1, 0]

models_to_evaluate = {
    "MajorityBaseline": MajorityClassEstimator().fit(X_test_data, y_test_data),
    "ThresholdClassifier": ThresholdClassifier(threshold=0.5).fit(X_test_data, y_test_data)
}

leaderboard_results = evaluate_estimators(models_to_evaluate, X_test_data, y_test_data)
print("\nQ10 Polymorphic Evaluator Leaderboard:")
for model_label, accuracy_score in leaderboard_results.items():
    print(f"    {model_label:<22}: {accuracy_score:.2%}")





    