# Day 27 — Exception Handling

📌 **Overview**

Day 27 begins Phase 3: Error Handling & Files, focusing on writing resilient, fault-tolerant Python applications.

Exceptions are runtime events that disrupt normal program flow when unexpected events occur (such as missing keys, invalid data types, divide-by-zero, or missing files). In Data Science pipelines, robust exception handling ensures that a single corrupted record or network hiccup does not abort long-running ingestion, data scraping, or machine learning batch inferences.

---

📚 **Topics Covered**

* Syntax Errors vs. Exceptions
* The `try-except` block mechanics
* Handling specific exceptions vs. avoiding bare `except:`
* The `else` and `finally` clauses
* Catching multiple exceptions (tuple syntax and multiple blocks)
* Accessing exception details (`as err`)
* Manually triggering errors (`raise`) and exception chaining (`from`)
* Building custom domain-specific Exception classes
* Error logging and safe degradation patterns in data ingestion

---
