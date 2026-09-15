# ==========================================
# Day 31 — Python Classes & Objects
# Script: classes_and_objects.py
# ==========================================

print("=== 1. DEFINING A CLASS & INSTANTIATING OBJECTS ===")
class ModelReport:
    """A user-defined class blueprint."""
    pass

report_1 = ModelReport()
report_2 = ModelReport()

print("Instance 1:", report_1)
print("Instance 2:", report_2)
print("Are they the same object in memory?:", report_1 is report_2)
print("Is report_1 an instance of ModelReport?:", isinstance(report_1, ModelReport))


print("\n=== 2. INSTANCE METHODS & THE SELF PARAMETER ===")
class LinearRegressionBaseline:
    framework = "Custom-ML"  # Class attribute

    def set_parameters(self, slope, intercept):
        self.slope = slope          # Instance attribute
        self.intercept = intercept  # Instance attribute

    def predict(self, x):
        return (self.slope * x) + self.intercept

model_a = LinearRegressionBaseline()
model_a.set_parameters(slope=2.0, intercept=10.0)

print(f"Framework: {model_a.framework}")
print(f"Parameters: slope={model_a.slope}, intercept={model_a.intercept}")
print(f"Prediction for x=5: {model_a.predict(5)}")


print("\n=== 3. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES ===")
class ExperimentTracker:
    total_runs = 0  # Shared class attribute

    def log_run(self, experiment_name, score):
        self.name = experiment_name  # Unique to this instance
        self.score = score           # Unique to this instance
        ExperimentTracker.total_runs += 1

run_1 = ExperimentTracker()
run_1.log_run("Experiment_Alpha", 0.89)

run_2 = ExperimentTracker()
run_2.log_run("Experiment_Beta", 0.94)

print(f"Run 1 -> Name: {run_1.name}, Score: {run_1.score}")
print(f"Run 2 -> Name: {run_2.name}, Score: {run_2.score}")
print("Total Experiments Run (Class State):", ExperimentTracker.total_runs)


print("\n=== 4. INSPECTING OBJECT STATE ===")
print("model_a __dict__:", model_a.__dict__)
print("Has 'slope'?:", hasattr(model_a, "slope"))
print("Get 'intercept':", getattr(model_a, "intercept"))
print("Get missing 'learning_rate' (fallback):", getattr(model_a, "learning_rate", 0.01))


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Basic Class Instantiation
class Dataset:
    def set_metadata(self, name, size):
        self.name = name
        self.size = size

ds1 = Dataset()
ds1.set_metadata("Iris", 150)

ds2 = Dataset()
ds2.set_metadata("Titanic", 891)

print(f"Q1 ds1: {ds1.name} ({ds1.size} rows) | ds2: {ds2.name} ({ds2.size} rows)")


# Q2 — The self Check
class IdentityVerifier:
    def show_identity(self):
        return id(self)

id_obj = IdentityVerifier()
print(f"Q2 External id: {id(id_obj)} | Internal self id: {id_obj.show_identity()} | Identical: {id(id_obj) == id_obj.show_identity()}")


# Q3 — Class vs Instance Attribute Counter
class Experiment:
    total_runs = 0

    def execute(self, run_name):
        self.run_name = run_name
        Experiment.total_runs += 1

e1 = Experiment()
e1.execute("Run_101")
e2 = Experiment()
e2.execute("Run_102")
print(f"Q3 Total runs logged: {Experiment.total_runs}")


# Q4 — Modifying State via Methods
class BankAccount:
    def initialize(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance

account = BankAccount()
account.initialize("Aman", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(f"Q4 Final balance for {account.owner}: ${account.balance}")


# Q5 — Dynamic Attribute Assignment
class EmptyContainer:
    pass

container = EmptyContainer()
container.status = "SUCCESS"
container.code = 200
container.execution_time = 0.042

print("Q5 Dynamically assigned attributes:", container.__dict__)


# Q6 — Built-in isinstance Validation
def validate_estimator(model):
    if not isinstance(model, LinearRegressionBaseline):
        raise TypeError("Object is not a valid LinearRegressionBaseline instance!")
    return "Validation Passed"

print("Q6 Model check:", validate_estimator(model_a))
try:
    validate_estimator(container)
except TypeError as err:
    print("Q6 Caught invalid type check:", err)


# Q7 — Attribute Checker
print("Q7 Safe retrieval of lr:", getattr(model_a, "learning_rate", 0.005))


# Q8 — Custom String Description Method
class Metric:
    def set_metric(self, name, score):
        self.name = name
        self.score = score

    def get_summary(self):
        return f"Metric <{self.name}>: {self.score:.4f}"

m = Metric()
m.set_metric("F1-Score", 0.8954)
print("Q8 Summary:", m.get_summary())


# Q9 — Metric Comparator
class EvaluationScore:
    def set_score(self, accuracy):
        self.accuracy = accuracy

    def is_better_than(self, other):
        if not isinstance(other, EvaluationScore):
            raise TypeError("Can only compare with another EvaluationScore instance")
        return self.accuracy > other.accuracy

eval_a = EvaluationScore()
eval_a.set_score(0.92)

eval_b = EvaluationScore()
eval_b.set_score(0.88)

print(f"Q9 Is Model A ({eval_a.accuracy}) better than Model B ({eval_b.accuracy})?: {eval_a.is_better_than(eval_b)}")


# Q10 — Challenge 🔥 (Simulating Scikit-Learn's StandardScaler)
class SimpleStandardScaler:
    def fit(self, data):
        """Calculates and stores the mean and standard deviation."""
        n = len(data)
        if n < 2:
            raise ValueError("Need at least 2 data points to compute standard deviation.")
        self.mean_ = sum(data) / n
        variance = sum((x - self.mean_) ** 2 for x in data) / n
        self.std_ = variance ** 0.5
        return self

    def transform(self, data):
        """Normalizes data using fitted mean and std."""
        if not hasattr(self, "mean_") or not hasattr(self, "std_"):
            raise RuntimeError("Estimator not fitted yet! Call 'fit' before 'transform'.")
        if self.std_ == 0:
            return [0.0 for _ in data]
        return [round((x - self.mean_) / self.std_, 4) for x in data]

    def fit_transform(self, data):
        """Fits to data, then transforms it."""
        return self.fit(data).transform(data)

scaler = SimpleStandardScaler()

# Testing runtime guard
try:
    scaler.transform([10, 20, 30])
except RuntimeError as e:
    print("Q10 Caught expected unfitted error:", e)

# Fitting and transforming
raw_dataset = [10.0, 20.0, 30.0, 40.0, 50.0]
scaled_dataset = scaler.fit_transform(raw_dataset)

print(f"Q10 Fitted Mean: {scaler.mean_} | Fitted Std: {scaler.std_:.4f}")
print("Q10 Scaled Data (mean=0, std=1):", scaled_dataset)



