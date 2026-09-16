# ==========================================
# Day 32 — Python __init__ Constructor
# Script: init_constructor.py
# ==========================================

print("=== 1. INITIALIZING INSTANCE STATE ===")
class ModelConfig:
    def __init__(self, model_type, max_depth=5, learning_rate=0.01):
        self.model_type = model_type
        self.max_depth = max_depth
        self.learning_rate = learning_rate

config_a = ModelConfig("RandomForest", max_depth=12)
config_b = ModelConfig("LogisticRegression", learning_rate=0.05)

print(f"Model A: {config_a.model_type} | Depth: {config_a.max_depth} | LR: {config_a.learning_rate}")
print(f"Model B: {config_b.model_type} | Depth: {config_b.max_depth} | LR: {config_b.learning_rate}")


print("\n=== 2. CONSTRUCTOR VALIDATION & DERIVED ATTRIBUTES ===")
class DatasetSplit:
    def __init__(self, name, test_size=0.2):
        if not isinstance(test_size, (int, float)):
            raise TypeError("test_size must be numeric")
        if not (0.0 < test_size < 1.0):
            raise ValueError(f"test_size must be between 0.0 and 1.0. Given: {test_size}")
        
        self.name = name
        self.test_size = float(test_size)
        # Derived attribute computed directly in constructor
        self.train_size = round(1.0 - self.test_size, 4)

split_1 = DatasetSplit("Churn_Data", test_size=0.25)
print(f"Dataset '{split_1.name}': Train={split_1.train_size:.2%}, Test={split_1.test_size:.2%}")

try:
    DatasetSplit("Corrupt_Split", test_size=1.5)
except ValueError as e:
    print("Caught validation error successfully:", e)


print("\n=== 3. __STR__ AND __REPR__ ===")
class MetricRecord:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"MetricRecord(name={self.name!r}, score={self.score})"

    def __str__(self):
        return f"Metric: {self.name} -> {self.score:.2%}"

f1_metric = MetricRecord("F1-Score", 0.912)
print("repr():", repr(f1_metric))
print("str(): ", str(f1_metric))


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Basic Parameterized Initialization
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user1 = User("alex99", "alex@domain.org")
print(f"Q1 User: {user1.username} ({user1.email})")


# Q2 — Default Constructor Values
class DatabaseConnector:
    def __init__(self, host="localhost", port=5432, database="analytics"):
        self.host = host
        self.port = port
        self.database = database
        self.connection_url = f"postgresql://{self.host}:{self.port}/{self.database}"

db = DatabaseConnector()
print("Q2 Default DB Connection URL:", db.connection_url)


# Q3 — Constructor Type and Value Guard
class Player:
    def __init__(self, name, health=100):
        if not isinstance(health, int):
            raise TypeError("health must be an integer")
        if not (0 <= health <= 100):
            raise ValueError(f"health must be between 0 and 100, got: {health}")
        self.name = name
        self.health = health

p1 = Player("Knight", 85)
print(f"Q3 Player created: {p1.name} with {p1.health} HP")
try:
    Player("Ghost", 150)
except ValueError as err:
    print("Q3 Caught invalid health guard:", err)


# Q4 — Derived Instance State
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = 2 * (width + height)

rect = Rectangle(10, 5)
print(f"Q4 Rectangle {rect.width}x{rect.height} -> Area: {rect.area}, Perimeter: {rect.perimeter}")


# Q5 — Developer Representation (__repr__)
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"

pt = Point2D(4.5, -9.2)
print("Q5 Point repr:", repr(pt))


# Q6 — Optional Dynamic Containers
class Experiment:
    def __init__(self, exp_id, tags=None):
        self.exp_id = exp_id
        # Safe mutable initialization
        self.tags = [] if tags is None else list(tags)

e1 = Experiment("EXP-01")
e1.tags.append("CV")
e2 = Experiment("EXP-02")

print(f"Q6 E1 Tags: {e1.tags} | E2 Tags: {e2.tags} (Independent: {e1.tags is not e2.tags})")


# Q7 — Auto-Incrementing Instance ID
class Job:
    _id_counter = 1000

    def __init__(self, task_name):
        Job._id_counter += 1
        self.job_id = Job._id_counter
        self.task_name = task_name

j1 = Job("Data Ingestion")
j2 = Job("Model Training")
j3 = Job("Model Deployment")
print(f"Q7 Assigned IDs: {j1.task_name} -> {j1.job_id}, {j2.task_name} -> {j2.job_id}, {j3.task_name} -> {j3.job_id}")


# Q8 — Unpacking Arguments into __init__
class Observation:
    def __init__(self, sensor, temp, humidity):
        self.sensor = sensor
        self.temp = temp
        self.humidity = humidity

payload = {"sensor": "SENS-North", "temp": 24.8, "humidity": 62}
obs = Observation(**payload)
print(f"Q8 Unpacked Observation: Sensor={obs.sensor}, Temp={obs.temp}C, Humidity={obs.humidity}%")


# Q9 — Constructor Return Guard
class BrokenConstructor:
    def __init__(self):
        pass
        # Writing 'return 42' raises TypeError: __init__() should return None, not 'int'

try:
    def bad_init(self):
        return 42
    BrokenConstructor.__init__ = bad_init
    BrokenConstructor()
except TypeError as err:
    print("Q9 Caught constructor return violation:", err)


# Q10 — Challenge 🔥 (Self-Contained KNN Classifier Stub)
class KNearestNeighborsStub:
    def __init__(self, k=3, distance_metric="euclidean"):
        if not isinstance(k, int):
            raise TypeError("k must be an integer")
        if k < 1 or k % 2 == 0:
            raise ValueError(f"k must be an odd positive integer. Given: {k}")
        
        valid_metrics = {"euclidean", "manhattan"}
        if distance_metric.lower() not in valid_metrics:
            raise ValueError(f"distance_metric must be one of {valid_metrics}. Given: {distance_metric}")

        self.k = k
        self.distance_metric = distance_metric.lower()
        self.is_fitted = False

    def fit(self, X, y):
        self.is_fitted = True
        return self

    def __repr__(self):
        return f"KNearestNeighborsStub(k={self.k}, distance_metric='{self.distance_metric}', is_fitted={self.is_fitted})"

knn_valid = KNearestNeighborsStub(k=5, distance_metric="Manhattan")
print("\nQ10 KNN Estimator Initialized:", repr(knn_valid))
knn_valid.fit([], [])
print("    KNN Estimator After Fitting:", repr(knn_valid))

try:
    KNearestNeighborsStub(k=4)  # Even k should fail
except ValueError as e:
    print("    Expected rejection of even k:", e)




    