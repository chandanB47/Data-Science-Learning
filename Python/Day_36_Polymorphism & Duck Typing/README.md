# Day 36 — Polymorphism & Duck Typing

📌 **Overview**

Day 36 covers Polymorphism, the fourth core pillar of Object-Oriented Programming in Python.

Polymorphism (meaning "many forms") allows different classes to define the same interface or method signature while implementing unique internal behaviors. In Python, polymorphism is driven by **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."* Python doesn't require explicit interfaces or base type declarations to invoke methods on an object.

In Data Science, polymorphism is the underlying principle behind uniform APIs. For example, in scikit-learn, you can swap `RandomForestClassifier`, `LogisticRegression`, and `SVC` inside cross-validation routines without changing code because all estimators adhere to the exact same `.fit(X, y)` and `.predict(X)` polymorphic contract.

---

📚 **Topics Covered**

* What is Polymorphism in Object-Oriented Design?
* Method Overriding as Polymorphism
* Duck Typing in Python (Dynamic typing vs. static interface enforcement)
* Polymorphism with Functions and Iterables
* Abstract Base Classes (ABCs) using `abc.ABC` and `@abstractmethod`
* Operator Overloading (Special Dunder Methods: `__add__`, `__len__`, `__eq__`)
* Building interchangeable model and transformation components

---

### 1. Duck Typing & Uniform Method Calling
Unlike languages like Java or C++, Python does not check whether an object belongs to a specific inheritance hierarchy before calling a method. As long as the object provides the requested method, Python executes it.

```python
class CSVLoader:
    def load(self, source):
        return f"Parsed CSV rows from {source}"

class JSONLoader:
    def load(self, source):
        return f"Parsed JSON dictionary from {source}"

def ingest_data(loader, source):
    # Polymorphic call: agnostic to the loader's concrete class
    return loader.load(source)

print(ingest_data(CSVLoader(), "data.csv"))
print(ingest_data(JSONLoader(), "data.json"))
