# Day 33 — Class Methods, Instance Methods & Static Methods

📌 **Overview**

Day 33 covers the three distinct method types available in Python Object-Oriented Programming:
1. **Instance Methods** (`self`)
2. **Class Methods** (`@classmethod`, `cls`)
3. **Static Methods** (`@staticmethod`)

Understanding the distinction between these methods is essential when designing maintainable Python packages and Data Science frameworks. They allow you to define methods that operate on individual object instances, implement alternative constructors that parse files/dictionaries/JSON into class instances, and group self-contained utility functions under a common namespace.

---

📚 **Topics Covered**

* Comparing the three method types: Instance vs. Class vs. Static
* The `@classmethod` decorator and the `cls` parameter
* Designing **Alternative Constructors** (e.g., `.from_csv()`, `.from_dict()`, `.from_json()`)
* The `@staticmethod` decorator for utility functions
* Mutating class-level state safely via class methods
* Dynamic dispatch and inheritance behavior with `cls`
* Best practices: When to use which method in Data Science pipelines

---
