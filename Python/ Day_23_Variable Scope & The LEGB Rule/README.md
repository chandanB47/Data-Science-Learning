# Day 23 — Variable Scope & The LEGB Rule

📌 **Overview**

Day 23 covers variable scope, namespaces, lifetime management, and name resolution in Python using the **LEGB Rule** (**L**ocal, **E**nclosing, **G**lobal, **B**uilt-in).

Scope determines where a variable is recognized and accessible in your code. In Data Science workflows, understanding scope prevents data-leakage bugs, avoids accidental global state mutations across notebook cells, and enables the creation of stateful closure functions for data processing pipelines.

---

📚 **Topics Covered**

* Understanding Namespaces and Variable Lifetimes
* The **LEGB** Hierarchy Rule
* Local Scope (`locals()`) vs Global Scope (`globals()`)
* Mutating global state with the `global` keyword
* Closures and nested scope manipulation with `nonlocal`
* Avoiding Common Scope Pitfalls (Shadowing built-ins, `UnboundLocalError`)
* Factory Functions and Stateful Closures for Data Transformers

---
