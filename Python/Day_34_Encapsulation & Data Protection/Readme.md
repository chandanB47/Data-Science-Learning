# Day 34 — Encapsulation & Data Protection

📌 **Overview**

Day 34 covers Encapsulation, one of the four foundational pillars of Object-Oriented Programming (alongside Abstraction, Inheritance, and Polymorphism).

Encapsulation bundles data (attributes) and methods that operate on that data into a single cohesive unit, while restricting direct external access to an object's internal state. 

In Data Science frameworks (such as scikit-learn estimators or database adapters), encapsulation protects internal parameters (like model weights, feature names, or connection pools) from being overwritten or corrupted by external code, providing controlled access via properties, getters, and setters.

---

📚 **Topics Covered**

* What is Encapsulation and Data Hiding?
* Public attributes and methods (default behavior)
* Protected members and the single-underscore (`_`) convention
* Private members and double-underscore (`__`) Name Mangling
* The Pythonic approach to Getters and Setters: The `@property` decorator
* Validation and constraints with property setters (`@<attr>.setter`)
* Read-only properties and deleter hooks (`@<attr>.deleter`)
* Practical scenario: Protecting Model Weights and Hyperparameters

---

### 1. Public, Protected, and Private Members

Python uses naming conventions to convey intent and enforce access levels:

| Level | Syntax | Access Scope | Enforced by Language? |
|---|---|---|:---:|
| **Public** | `self.attribute` | Anywhere (internal and external) | No restriction |
| **Protected** | `self._attribute` | Internal class and subclasses | No (gentlemen's agreement convention) |
| **Private** | `self.__attribute` | Inside defining class only | **Yes (via Name Mangling)** |

```python
class ModelSecurity:
    def __init__(self, name, version, secret_token):
        self.name = name                 # Public
        self._version = version          # Protected (internal use signal)
        self.__secret_token = secret_token  # Private (mangled)

m = ModelSecurity("RiskModel", 1.2, "SEC_KEY_891")
print(m.name)              # RiskModel
print(m._version)          # 1.2 (accessible, but violates convention)

# Direct access to private member raises AttributeError
# print(m.__secret_token)  # AttributeError: 'ModelSecurity' object has no attribute '__secret_token'
