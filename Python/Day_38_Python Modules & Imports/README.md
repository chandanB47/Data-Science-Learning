# Day 38 — Python Modules & Imports

📌 **Overview**

Day 38 begins **Phase 5: Python Ecosystem, Modules & Environments**.

A **module** is simply a Python file (`.py`) containing executable statements, function definitions, classes, and variables intended to be reused across different programs. Modular programming decomposes large, monolithic scripts into maintainable, self-contained units.

In Data Science and production engineering, modularization is essential for organizing feature engineering scripts, model architectures, database connectors, and evaluation pipelines into clean, importable libraries.

---

📚 **Topics Covered**

* What is a Module? (`module.py`)
* Import semantics and variants:
  * `import module`
  * `import module as alias`
  * `from module import function, Class`
  * `from module import *` (and why it is an anti-pattern)
* The Module Search Path: `sys.path` and environment resolution
* Module caching: `sys.modules` and reload mechanics (`importlib.reload`)
* The `if __name__ == "__main__":` idiom explained
* Controlling public module exports using `__all__`
* Inspecting modules with `dir()`, `__file__`, `__name__`, and `__doc__`
* Building a modular feature engineering pipeline

---

### 1. The Import Mechanics & Variants

| Import Syntax | Namespace Effect | Usage Example |
|---|---|---|
| `import math` | Keeps module namespace clean | `math.sqrt(25)` |
| `import numpy as np` | Provides a standard shortened alias | `np.mean(data)` |
| `from math import sqrt, pi` | Imports specific identifiers into local scope | `sqrt(25)` |
| `from math import *` | **Anti-pattern**: Pollutes local namespace with shadows | Avoid in production |

---

### 2. The `if __name__ == "__main__":` Idiom
When Python executes a source file directly, it sets the special variable `__name__` to `"__main__"`. When the file is imported as a module by another script, `__name__` is set to the module's file/module name.

```python
# metrics_utils.py

def accuracy(y_true, y_pred):
    return sum(yt == yp for yt, yp in zip(y_true, y_pred)) / len(y_true)

# Unit test block runs ONLY when executed directly, NOT when imported
if __name__ == "__main__":
    print("[TEST] Running local test suite...")
    test_true = [1, 0, 1, 1]
    test_pred = [1, 0, 1, 0]
    print(f"Test Accuracy: {accuracy(test_true, test_pred):.2%}")
