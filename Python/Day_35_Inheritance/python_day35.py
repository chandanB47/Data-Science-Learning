# ==========================================
# Day 35 — Python Inheritance
# Script: inheritance.py
# ==========================================

print("=== 1. SINGLE INHERITANCE & SUPER() ===")
class BaseDataset:
    def __init__(self, name, row_count):
        self.name = name
        self.row_count = row_count

    def get_summary(self):
        return f"Dataset: '{self.name}' | Rows: {self.row_count:,}"

class LabeledDataset(BaseDataset):
    def __init__(self, name, row_count, target_col):
        # Delegate initialization to parent
        super().__init__(name, row_count)
        self.target_col = target_col

    # Method Overriding: Augmenting parent method
    def get_summary(self):
        base_summary = super().get_summary()
        return f"{base_summary} | Target Column: '{self.target_col}'"

ds = LabeledDataset("CustomerChurn", 10000, "Churned")
print(ds.get_summary())


print("\n=== 2. MULTILEVEL INHERITANCE ===")
class HardwareResource:
    def __init__(self, device_id):
        self.device_id = device_id

class ComputeNode(HardwareResource):
    def __init__(self, device_id, cpu_cores):
        super().__init__(device_id)
        self.cpu_cores = cpu_cores

class GPUAcceleratedNode(ComputeNode):
    def __init__(self, device_id, cpu_cores, gpu_model, vram_gb):
        super().__init__(device_id, cpu_cores)
        self.gpu_model = gpu_model
        self.vram_gb = vram_gb

node = GPUAcceleratedNode("NODE-901", cpu_cores=32, gpu_model="NVIDIA A100", vram_gb=80)
print(f"Node: {node.device_id} | CPU Cores: {node.cpu_cores} | GPU: {node.gpu_model} ({node.vram_gb} GB VRAM)")


print("\n=== 3. MULTIPLE INHERITANCE & MIXINS ===")
class JSONSerializableMixin:
    def to_json_dict(self):
        return {"data": self.__dict__}

class HTMLDisplayMixin:
    def to_html(self):
        items = "".join(f"<li>{k}: {v}</li>" for k, v in self.__dict__.items())
        return f"<ul>{items}</ul>"

class ExperimentResult(JSONSerializableMixin, HTMLDisplayMixin):
    def __init__(self, run_id, score):
        self.run_id = run_id
        self.score = score

exp = ExperimentResult("EXP_001", 0.945)
print("JSON Mixin Output:", exp.to_json_dict())
print("HTML Mixin Output:", exp.to_html())
print("Method Resolution Order (MRO):", [cls.__name__ for cls in ExperimentResult.mro()])


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Basic Single Inheritance
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

class ElectricCar(Vehicle):
    def __init__(self, brand, max_speed, battery_kwh):
        super().__init__(brand, max_speed)
        self.battery_kwh = battery_kwh

ev = ElectricCar("Tesla", 250, 75)
print(f"Q1 EV: {ev.brand} | Top Speed: {ev.max_speed} km/h | Battery: {ev.battery_kwh} kWh")


# Q2 — Constructor Delegation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

mgr = Manager("Priya", 120000, "Data Science")
print(f"Q2 Manager: {mgr.name}, Salary: ${mgr.salary:,}, Dept: {mgr.department}")


# Q3 — Method Augmentation
class Preprocessor:
    def clean(self, text):
        return text.strip()

class TextPreprocessor(Preprocessor):
    def clean(self, text):
        cleaned = super().clean(text)
        return cleaned.lower()

tp = TextPreprocessor()
print(f"Q3 TextPreprocessor: '{tp.clean('   DATA ENGINEERING   ')}'")


# Q4 — Multilevel Inheritance
class Device:
    def __init__(self, power_watts):
        self.power_watts = power_watts

class Computer(Device):
    def __init__(self, power_watts, os_name):
        super().__init__(power_watts)
        self.os_name = os_name

class Laptop(Computer):
    def __init__(self, power_watts, os_name, weight_kg):
        super().__init__(power_watts, os_name)
        self.weight_kg = weight_kg

lap = Laptop(65, "Ubuntu 24.04", 1.4)
print(f"Q4 Laptop: {lap.os_name} | Power: {lap.power_watts}W | Weight: {lap.weight_kg}kg")


# Q5 — Multiple Inheritance Mixin
class AuditMixin:
    def generate_audit_id(self):
        return f"AUDIT_{id(self)}"

class SerializableMixin:
    def get_state(self):
        return dict(self.__dict__)

class AnalyticalDataset(AuditMixin, SerializableMixin):
    def __init__(self, name):
        self.name = name

ads = AnalyticalDataset("Telecom_Records")
print(f"Q5 Dataset: {ads.name} | Audit ID: {ads.generate_audit_id()} | State: {ads.get_state()}")


# Q6 — Inspecting MRO (Diamond Problem)
class A:
    def ping(self):
        return "A"

class B(A):
    def ping(self):
        return "B"

class C(A):
    def ping(self):
        return "C"

class D(B, C):
    pass

d_obj = D()
print(f"Q6 D().ping() resolves to: {d_obj.ping()}")
print("   MRO path for D:", [c.__name__ for c in D.mro()])


# Q7 — isinstance vs issubclass
print(f"Q7 issubclass(Laptop, Device): {issubclass(Laptop, Device)}")
print(f"   isinstance(lap, Device):   {isinstance(lap, Device)}")
print(f"   issubclass(Device, Laptop): {issubclass(Device, Laptop)}")


# Q8 — Preventing Parent Override / Explicit Calling
class BaseWorker:
    def execute(self):
        return "Base task execution"

class SpecialWorker(BaseWorker):
    def execute(self):
        parent_action = super().execute()
        return f"{parent_action} + Custom specialized routine"

worker = SpecialWorker()
print("Q8 Execution:", worker.execute())


# Q9 — Abstract Interface Enforcement
class BaseModelInterface:
    def predict(self, X):
        raise NotImplementedError("Subclasses must implement 'predict(X)' method!")

class DummyModel(BaseModelInterface):
    pass

try:
    DummyModel().predict([1, 2, 3])
except NotImplementedError as err:
    print("Q9 Caught expected abstract error:", err)


# Q10 — Challenge 🔥 (Hierarchical Machine Learning Model Pipeline)
class BaseEstimator:
    def __init__(self, model_name):
        self.model_name = model_name

    def get_params(self):
        return {"model_name": self.model_name}

class SupervisedEstimator(BaseEstimator):
    def __init__(self, model_name, target_column):
        super().__init__(model_name)
        self.target_column = target_column
        self.is_fitted = False

    def fit(self, X, y):
        raise NotImplementedError("Every SupervisedEstimator subclass must implement 'fit(X, y)'!")

    def get_params(self):
        params = super().get_params()
        params["target_column"] = self.target_column
        params["is_fitted"] = self.is_fitted
        return params

class LinearClassifier(SupervisedEstimator):
    def __init__(self, model_name="LinearClassifier", target_column="target", learning_rate=0.01):
        super().__init__(model_name, target_column)
        self.learning_rate = learning_rate
        self.classes_ = []
        self.weights_ = []

    def fit(self, X, y):
        # Simulated fit logic
        self.classes_ = sorted(list(set(y)))
        self.weights_ = [0.1 * (i + 1) for i in range(len(X[0]))]
        self.is_fitted = True
        return self

    def predict(self, X):
        if not self.is_fitted:
            raise RuntimeError("Model is not fitted. Call 'fit' before 'predict'.")
        # Dot product with weights for binary thresholding
        predictions = []
        for sample in X:
            score = sum(w * x for w, x in zip(self.weights_, sample))
            predictions.append(self.classes_[1] if score > 0.5 else self.classes_[0])
        return predictions

    def get_params(self):
        params = super().get_params()
        params["learning_rate"] = self.learning_rate
        return params

# Verification
clf = LinearClassifier(target_column="default_payment", learning_rate=0.05)
print("\nQ10 Model Initialized Params:", clf.get_params())

X_sample = [[1.2, 0.5], [2.1, 3.4], [0.2, 0.1]]
y_sample = [0, 1, 0]

clf.fit(X_sample, y_sample)
print("    Fitted Classes:", clf.classes_)
print("    Learned Weights:", clf.weights_)
print("    Predictions on X_sample:", clf.predict(X_sample))
print("    Updated Params:", clf.get_params())



