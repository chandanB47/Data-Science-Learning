# ==========================================
# Day 34 — Python Encapsulation
# Script: encapsulation.py
# ==========================================

import math

print("=== 1. PUBLIC, PROTECTED & PRIVATE MEMBERS ===")
class AccessDemo:
    def __init__(self, public_val, protected_val, private_val):
        self.public_val = public_val
        self._protected_val = protected_val
        self.__private_val = private_val

    def read_private(self):
        # Internal access to private attribute
        return f"Internal access to private: {self.__private_val}"

demo = AccessDemo("PUBLIC", "PROTECTED", "PRIVATE")

print("Public attribute:   ", demo.public_val)
print("Protected attribute:", demo._protected_val)  # Accessible, but violates convention

try:
    print(demo.__private_val)
except AttributeError as err:
    print("Private access failed as expected:", err)

print(demo.read_private())


print("\n=== 2. NAME MANGLING MECHANICS ===")
print("Instance __dict__ keys:", list(demo.__dict__.keys()))
# Demonstrating mangled attribute retrieval (for debugging/inspection)
mangled_key = "_AccessDemo__private_val"
print(f"Direct access via mangled name '{mangled_key}':", getattr(demo, mangled_key))


print("\n=== 3. GETTERS AND SETTERS VIA @PROPERTY ===")
class HyperparameterConfig:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate  # Triggers property setter

    @property
    def learning_rate(self):
        """Getter for learning_rate."""
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        """Setter with validation bounds."""
        if not isinstance(value, (int, float)):
            raise TypeError("learning_rate must be a numeric float or int")
        if not (0.0 < value < 1.0):
            raise ValueError(f"learning_rate must be strictly between 0 and 1. Received: {value}")
        self._learning_rate = float(value)

hp = HyperparameterConfig(0.05)
print("Configured Learning Rate:", hp.learning_rate)

hp.learning_rate = 0.001
print("Updated Learning Rate:   ", hp.learning_rate)

try:
    hp.learning_rate = 1.5
except ValueError as e:
    print("Caught invalid hyperparameter update:", e)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Naming Level Showcase
class Showcase:
    def __init__(self):
        self.data_level = "Level 1: Public"
        self._dev_flag = "Level 2: Protected (Do not touch outside class)"
        self.__security_hash = "Level 3: Private (Mangled)"

sc = Showcase()
print(f"Q1 {sc.data_level} | {sc._dev_flag}")


# Q2 — Name Mangling Inspection
print(f"Q2 Name Mangled Key in dict: '{[k for k in sc.__dict__ if k.startswith('_Showcase')][0]}'")


# Q3 — Property Getter and Setter
class TemperatureSensor:
    def __init__(self, celsius=0.0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature cannot drop below absolute zero (-273.15C). Got: {value}")
        self._celsius = float(value)

sensor = TemperatureSensor(25.0)
print("Q3 Initial Celsius:", sensor.celsius)
try:
    sensor.celsius = -300.0
except ValueError as err:
    print("Q3 Caught absolute zero violation:", err)


# Q4 — Computed Dynamic Property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return round(math.pi * (self.radius ** 2), 4)

c = Circle(5.0)
print(f"Q4 Circle (radius={c.radius}) -> Computed Area: {c.area}")


# Q5 — Two-Way Unit Conversion
class DualTemperatureSensor(TemperatureSensor):
    @property
    def fahrenheit(self):
        return round((self.celsius * 9 / 5) + 32, 2)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

dual_sensor = DualTemperatureSensor(100.0)
print(f"Q5 Boiling: {dual_sensor.celsius}°C == {dual_sensor.fahrenheit}°F")
dual_sensor.fahrenheit = 32.0
print(f"   Freezing Set via F: {dual_sensor.celsius}°C == {dual_sensor.fahrenheit}°F")


# Q6 — Immutable Identifier
class ExperimentRun:
    def __init__(self, run_id):
        self._run_id = run_id

    @property
    def run_id(self):
        return self._run_id

run_entry = ExperimentRun("RUN_2026_A")
print("Q6 Extracted Run ID:", run_entry.run_id)
try:
    run_entry.run_id = "RUN_NEW"
except AttributeError as err:
    print("Q6 Mutation blocked on read-only attribute:", err)


# Q7 — Deleter Method
class SecureToken:
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @token.deleter
    def token(self):
        print("   [DELETER] Erasing secure token from memory...")
        self._token = None

sec = SecureToken("AUTH_BEARER_99812")
print("Q7 Token before:", sec.token)
del sec.token
print("Q7 Token after deletion:", sec.token)


# Q8 — String Property Sanitizer
class UserAccount:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Username cannot be empty")
        self._username = value.strip().lower()

account = UserAccount("   AnilKumar_DataScience   ")
print(f"Q8 Sanitized Username: '{account.username}'")


# Q9 — Private Helper Method
class IngestionPipeline:
    def process(self, raw_input):
        clean = self.__sanitize_input(raw_input)
        return f"Processed: {clean}"

    def __sanitize_input(self, text):
        return text.replace(";", "").strip()

pipeline = IngestionPipeline()
print("Q9 Public Process Call:", pipeline.process("SELECT * FROM users;   "))
print("Q9 Private helper is mangled:", hasattr(pipeline, "_IngestionPipeline__sanitize_input"))


# Q10 — Challenge 🔥 (Encapsulated Machine Learning Estimator State)
class SafeLinearModel:
    def __init__(self, regularization=0.0):
        self.regularization_strength = regularization
        self.__weights = None
        self.__bias = None
        self.__is_fitted = False

    @property
    def regularization_strength(self):
        return self._regularization

    @regularization_strength.setter
    def regularization_strength(self, value):
        if not isinstance(value, (int, float)) or value < 0.0:
            raise ValueError(f"Regularization must be non-negative. Got: {value}")
        self._regularization = float(value)

    def fit(self, weights: list, bias: float):
        """Simulate training and parameter assignment."""
        if not isinstance(weights, list) or not isinstance(bias, (int, float)):
            raise TypeError("Weights must be a list and bias a float/int.")
        self.__weights = list(weights)
        self.__bias = float(bias)
        self.__is_fitted = True
        return self

    @property
    def weights(self):
        if not self.__is_fitted:
            raise RuntimeError("Model is not fitted yet. Cannot access weights.")
        # Returning a copy to maintain internal encapsulation
        return list(self.__weights)

    @property
    def bias(self):
        if not self.__is_fitted:
            raise RuntimeError("Model is not fitted yet. Cannot access bias.")
        return self.__bias

    def predict(self, feature_vector):
        if not self.__is_fitted:
            raise RuntimeError("Model is not fitted yet. Cannot make predictions.")
        if len(feature_vector) != len(self.__weights):
            raise ValueError("Feature vector dimensions do not match model weights.")
        return sum(w * x for w, x in zip(self.__weights, feature_vector)) + self.__bias

# Instantiation
safe_model = SafeLinearModel(regularization=0.01)

# Verifying read-only protection prior to fitting
try:
    print(safe_model.weights)
except RuntimeError as err:
    print("\nQ10 Pre-fit weights access blocked:", err)

# Fitting the model
safe_model.fit(weights=[0.5, -1.2, 2.0], bias=0.1)

print("Q10 Fitted Model Parameters:")
print("   Weights:", safe_model.weights)
print("   Bias:   ", safe_model.bias)
print("   Prediction on [2, 1, 3]:", safe_model.predict([2, 1, 3]))




