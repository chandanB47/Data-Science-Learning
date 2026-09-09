# Day 29 — Working with CSV Files

📌 **Overview**

Day 29 covers reading, parsing, transforming, and writing Tabular CSV (Comma-Separated Values) data using Python's built-in `csv` module.

CSV is the universal plain-text standard for tabular data exchange in Analytics and Data Science. Before jumping into external third-party libraries like pandas, mastering the standard library's `csv.reader`, `csv.writer`, `csv.DictReader`, and `csv.DictWriter` is critical for memory-conscious streaming, custom dialect configuration, and low-level data pipeline engineering.

---

📚 **Topics Covered**

* Anatomy of CSV files and parsing challenges (commas in strings, quotes, delimiters)
* Reading rows as lists using `csv.reader`
* Handling headers and advancing iterators with `next()`
* Reading rows as ordered dictionaries using `csv.DictReader`
* Writing data using `csv.writer` (`writerow`, `writerows`)
* Writing dictionaries using `csv.DictWriter` and fieldname mapping
* Custom delimiters, quotes, and dialects (TSV, pipe-delimited, `csv.QUOTE_MINIMAL`)
* The `newline=''` convention across different operating systems
* Building an end-to-end data cleaning and filtering pipeline on CSVs

---
