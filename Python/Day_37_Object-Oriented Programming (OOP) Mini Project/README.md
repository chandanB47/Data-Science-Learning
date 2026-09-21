# Day 37 — Object-Oriented Programming (OOP) Mini Project

📌 **Overview**

Day 37 concludes Phase 4: Object-Oriented Programming with a comprehensive, end-to-end Mini Project: **The ML Experiment & Model Registry System**.

This production-style application consolidates all OOP and file-handling principles covered in Days 27–36 into a single cohesive architecture:
* **Classes & Instances** (`Day 31`)
* **`__init__` Constructors & Representation** (`Day 32`)
* **Class & Static Methods as Factory Deserializers** (`Day 33`)
* **Encapsulation & Property Guards** (`Day 34`)
* **Inheritance & `super()` Delegation** (`Day 35`)
* **Polymorphism, Abstract Base Classes (`ABC`), and Operator Overloading** (`Day 36`)
* **Exception Handling & File Persistence with JSON** (`Days 27 & 30`)

---

## 🏗️ System Architecture & Class Hierarchy

```text
               ┌───────────────────────┐
               │    BaseModel (ABC)    │  <<Abstract>>
               │  - fit(X, y)          │
               │  - predict(X)         │
               │  - evaluate(X, y)     │
               └──────────┬────────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
┌───────────────────────┐   ┌───────────────────────┐
│  MajorityClassifier   │   │  ThresholdClassifier  │
│  - learns mode class  │   │  - learns feature split│
└───────────────────────┘   └───────────────────────┘

┌────────────────────────────────────────────────────────┐
│               ExperimentRun (Record Class)             │
│  - Encapsulated metrics, parameters, and run metadata  │
│  - Operator Overloading: __eq__, __lt__                │
│  - Factory Constructors: .from_dict(), .to_dict()      │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│            ModelRegistry (Manager Class)               │
│  - Stores, compares, filters, and benchmarks runs     │
│  - JSON Disk Persistence: .save_to_disk(), .load()     │
└────────────────────────────────────────────────────────┘
