# Day 19 — Nested Data Structures

📌 **Overview**

Day 19 covers designing, navigating, updating, and querying complex nested data structures in Python.

Real-world datasets (such as REST API responses, JSON database documents, NoSQL collections, and web scraping trees) are rarely flat. They consist of multi-level compositions:
* Lists of Dictionaries (`List[Dict]`)
* Dictionaries of Lists (`Dict[List]`)
* Dictionaries of Dictionaries (`Dict[Dict]`)
* Multi-dimensional nested hierarchies

Mastering nested data structures is essential for preparing raw, semi-structured records before loading them into tabular pandas DataFrames.

---

📚 **Topics Covered**

* Anatomy of semi-structured data (`List[Dict]`, `Dict[List]`, `Dict[Dict]`)
* Multi-index and chained key-value lookups
* Safe traversal through deeply nested objects
* In-place mutation vs deep copying (`copy.deepcopy`)
* Nested comprehensions for extraction and restructuring
* Flattening multi-level hierarchical records into tabular rows
* Data aggregation and grouping across nested records

---
