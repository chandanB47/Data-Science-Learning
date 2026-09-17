# ==========================================
# Day 33 — Class, Instance & Static Methods
# Script: class_and_instance_methods.py
# ==========================================

print("=== 1. THE THREE METHOD TYPES ===")
class MethodDemo:
    class_name = "MethodDemo_v1"

    def __init__(self, instance_id):
        self.instance_id = instance_id

    # 1. Instance Method (binds to self)
    def instance_info(self):
        return f"Instance ID: {self.instance_id} | Class Name: {self.class_name}"

    # 2. Class Method (binds to cls)
    @classmethod
    def get_class_name(cls):
        return f"Invoked on Class: {cls.__name__} (Attribute: {cls.class_name})"

    # 3. Static Method (no automatic binding)
    @staticmethod
    def calculate_ratio(a, b):
        return round(a / b, 4) if b != 0 else 0.0

demo = MethodDemo("OBJ_401")
print("Instance Method:", demo.instance_info())
print("Class Method:   ", MethodDemo.get_class_name())
print("Static Method:  ", MethodDemo.calculate_ratio(15, 4))


print("\n=== 2. ALTERNATIVE CONSTRUCTORS (@classmethod) ===")
class DatasetConfig:
    def __init__(self, name, total_rows, feature_count):
        self.name = name
        self.total_rows = total_rows
        self.feature_count = feature_count

    def __repr__(self):
        return f"DatasetConfig(name='{self.name}', rows={self.total_rows}, features={self.feature_count})"

    @classmethod
    def from_dict(cls, payload):
        """Constructs an instance directly from an API dictionary."""
        return cls(
            name=payload["dataset_name"],
            total_rows=payload["rows"],
            feature_count=len(payload["columns"])
        )

    @classmethod
    def from_csv_line(cls, csv_line):
        """Constructs an instance directly from a comma-delimited string."""
        name, rows_str, feat_str = csv_line.strip().split(",")
        return cls(name=name, total_rows=int(rows_str), feature_count=int(feat_str))

cfg_direct = DatasetConfig("Direct", 100, 5)
cfg_dict = DatasetConfig.from_dict({
    "dataset_name": "API_Stream",
    "rows": 5000,
    "columns": ["age", "income", "target"]
})
cfg_csv = DatasetConfig.from_csv_line("Housing_Prices,1460,79")

print("Direct:   ", cfg_direct)
print("From Dict:", cfg_dict)
print("From CSV: ", cfg_csv)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Identify Method Types
class MethodShowcase:
    def inst_m(self):
        return "Bound to instance (self)"

    @classmethod
    def cls_m(cls):
        return f"Bound to class: {cls.__name__}"

    @staticmethod
    def stat_m():
        return "Unbound utility method"

showcase = MethodShowcase()
print("Q1 Instance:", showcase.inst_m())
print("Q1 Class:   ", MethodShowcase.cls_m())
print("Q1 Static:  ", MethodShowcase.stat_m())


# Q2 — CSV String Constructor
class Date:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    def __repr__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_dash_string(cls, date_str):
        y, m, d = date_str.split("-")
        return cls(y, m, d)

parsed_date = Date.from_dash_string("2026-09-17")
print(f"Q2 Parsed Date: {parsed_date} (Year: {parsed_date.year})")


# Q3 — Class-Level Instance Tracker
class AnalyticsWorker:
    _active_workers = 0

    def __init__(self, worker_id):
        self.worker_id = worker_id
        AnalyticsWorker._active_workers += 1

    @classmethod
    def get_worker_count(cls):
        return cls._active_workers

w1 = AnalyticsWorker("W1")
w2 = AnalyticsWorker("W2")
w3 = AnalyticsWorker("W3")
print(f"Q3 Active Workers Count: {AnalyticsWorker.get_worker_count()}")


# Q4 — Stateless Normalization Helper
class Scaler:
    @staticmethod
    def clamp(value, min_val, max_val):
        return max(min_val, min(max_val, value))

print("Q4 Clamped 125 (0, 100):", Scaler.clamp(125, 0, 100))
print("Q4 Clamped -15 (0, 100):", Scaler.clamp(-15, 0, 100))
print("Q4 Clamped 42  (0, 100):", Scaler.clamp(42, 0, 100))


# Q5 — Dict Deserializer
class HyperParameters:
    def __init__(self, n_estimators, max_depth, lr):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.lr = lr

    def __repr__(self):
        return f"HyperParameters(n_estimators={self.n_estimators}, max_depth={self.max_depth}, lr={self.lr})"

    @classmethod
    def from_dict(cls, d):
        return cls(
            n_estimators=d.get("n_estimators", 100),
            max_depth=d.get("max_depth", 6),
            lr=d.get("learning_rate", 0.01)
        )

raw_params = {"n_estimators": 250, "max_depth": 10, "learning_rate": 0.05}
hp = HyperParameters.from_dict(raw_params)
print("Q5 Deserialized Hyperparameters:", hp)


# Q6 — Factory from File Path
class LogConfig:
    def __init__(self, service, environment):
        self.service = service
        self.environment = environment

    @classmethod
    def from_filepath(cls, path_str):
        # path format: "/var/logs/{env}/{service}.log"
        parts = path_str.strip("/").split("/")
        env = parts[-2]
        service = parts[-1].replace(".log", "")
        return cls(service, env)

log_cfg = LogConfig.from_filepath("/var/logs/production/payment_gateway.log")
print(f"Q6 Log Config: Service='{log_cfg.service}', Env='{log_cfg.environment}'")


# Q7 — Static Validator Method
class CustomerRecord:
    def __init__(self, email):
        if not self.validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        self.email = email

    @staticmethod
    def validate_email(email):
        return isinstance(email, str) and "@" in email and "." in email.split("@")[-1]

print("Q7 'analyst@domain.com' valid?:", CustomerRecord.validate_email("analyst@domain.com"))
print("Q7 'invalid-email.com' valid?: ", CustomerRecord.validate_email("invalid-email.com"))


# Q8 — Class Mutation via Method
class AppConfig:
    TIMEOUT = 30

    @classmethod
    def set_timeout(cls, new_timeout):
        if new_timeout <= 0:
            raise ValueError("Timeout must be strictly positive")
        cls.TIMEOUT = new_timeout

AppConfig.set_timeout(60)
print("Q8 Updated AppConfig.TIMEOUT:", AppConfig.TIMEOUT)


# Q9 — Inheritance Dispatch with cls
class BaseEstimator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_default(cls):
        # Uses cls(), ensuring derived types return instances of the child
        return cls("DefaultModel")

class SpecializedRegressor(BaseEstimator):
    pass

base_obj = BaseEstimator.create_default()
child_obj = SpecializedRegressor.create_default()

print(f"Q9 base_obj type:  {type(base_obj).__name__}")
print(f"Q9 child_obj type: {type(child_obj).__name__} (Correctly dispatched via cls)")


# Q10 — Challenge 🔥 (Self-Instantiating Model Benchmark Registry)
class MLModelBenchmark:
    _registry = []

    def __init__(self, model_name, accuracy, latency_ms):
        self.model_name = model_name
        self.accuracy = accuracy
        self.latency_ms = latency_ms

    def __repr__(self):
        return f"Benchmark(model='{self.model_name}', acc={self.accuracy:.2%}, latency={self.latency_ms}ms)"

    @staticmethod
    def calculate_efficiency_score(accuracy, latency_ms):
        """Higher is better: accuracy scaled by latency."""
        if latency_ms <= 0:
            return 0.0
        return round((accuracy * 1000) / latency_ms, 2)

    @classmethod
    def register_run(cls, model_name, accuracy, latency_ms):
        if not (0.0 <= accuracy <= 1.0):
            raise ValueError(f"Accuracy must be in range [0, 1]. Given: {accuracy}")
        if latency_ms <= 0:
            raise ValueError(f"Latency must be positive. Given: {latency_ms}")

        instance = cls(model_name, accuracy, latency_ms)
        cls._registry.append(instance)
        return instance

    @classmethod
    def get_top_performer(cls):
        if not cls._registry:
            return None
        return max(cls._registry, key=lambda run: run.accuracy)

    @classmethod
    def clear_registry(cls):
        cls._registry.clear()

# Register benchmarking runs
MLModelBenchmark.register_run("RandomForest", 0.88, 45.0)
MLModelBenchmark.register_run("XGBoost", 0.94, 75.0)
MLModelBenchmark.register_run("LightGBM", 0.93, 30.0)
MLModelBenchmark.register_run("LogisticRegression", 0.82, 10.0)

print("\nQ10 Benchmark Runs Registered:", len(MLModelBenchmark._registry))
top_model = MLModelBenchmark.get_top_performer()
print(f"    Top Performer by Accuracy: {top_model}")

print("    Efficiency Scores (Acc * 1000 / Latency):")
for run in MLModelBenchmark._registry:
    eff = MLModelBenchmark.calculate_efficiency_score(run.accuracy, run.latency_ms)
    print(f"      {run.model_name:<20}: {eff}")



    