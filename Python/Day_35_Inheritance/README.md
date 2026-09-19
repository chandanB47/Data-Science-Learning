# Day 35 — Inheritance

📌 **Overview**

Day 35 covers Inheritance, a core Object-Oriented Programming (OOP) mechanism that enables a new class (child/subclass) to inherit attributes and methods from an existing class (parent/base class).

Inheritance promotes code reuse, eliminates boilerplate, and establishes logical hierarchical relationships ("is-a" relationships).

In Data Science frameworks (such as PyTorch's `nn.Module` or scikit-learn's `BaseEstimator` and `ClassifierMixin`), inheritance is the primary mechanism for standardizing interfaces, sharing common validation logic, and extending base algorithms without rewriting boilerplate fitting and scoring routines.

---

📚 **Topics Covered**

* What is Inheritance? (Base/Parent vs. Derived/Child Classes)
* Single Inheritance syntax
* The `super()` proxy object and constructor delegation
* Method Overriding (customizing base class behavior)
* Multilevel Inheritance chains
* Multiple Inheritance and Cooperative Multi-Parenting
* The Method Resolution Order (MRO) and `C3 Linearization` (`ClassName.mro()`)
* Checking class relationships: `issubclass()` and `isinstance()`
* Practical Data Science Scenario: Designing an Estimator Hierarchy (`BaseEstimator` $\to$ `Classifier`)

---

### 1. Single Inheritance & Constructor Delegation with `super()`
When a subclass defines its own `__init__`, it overrides the parent's constructor. Use `super().__init__(...)` to invoke the parent constructor and ensure base attributes are initialized properly.

```python
class BaseDataset:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def get_summary(self):
        return f"Dataset: {self.name} ({self.rows:,} rows)"

class LabeledDataset(BaseDataset):
    def __init__(self, name, rows, target_column):
        # Delegate initialization of name and rows to BaseDataset
        super().__init__(name, rows)
        self.target_column = target_column

ds = LabeledDataset("Titanic", 891, "Survived")
print(ds.get_summary())         # Inherited method: Dataset: Titanic (891 rows)
print(ds.target_column)         # Subclass attribute: Survived
