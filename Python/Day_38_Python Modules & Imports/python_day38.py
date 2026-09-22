# ==========================================
# Day 38 — Python Modules & Imports
# Script: python_day38.py
# ==========================================

import sys
import os
import types
import importlib


# ==========================================
# 1. UNDERSTANDING MODULE ATTRIBUTES & DIR()
# ==========================================

print("=== 1. UNDERSTANDING MODULE ATTRIBUTES & DIR() ===")

import math

print(f"Module Name:      {math.__name__}")
print(f"Module Docstring: {math.__doc__.strip()[:50]}...")
print(
    f"Public Symbols:   "
    f"{[s for s in dir(math) if not s.startswith('_')][:8]}"
)


# ==========================================
# 2. THE MODULE SEARCH PATH (SYS.PATH)
# ==========================================

print("\n=== 2. THE MODULE SEARCH PATH (SYS.PATH) ===")

print("First 3 entries in sys.path:")

for idx, path_entry in enumerate(sys.path[:3], start=1):
    print(f"  {idx}. {path_entry}")


# ==========================================
# 3. DYNAMIC MODULE CREATION & PERSISTENCE
# ==========================================

print("\n=== 3. DYNAMIC MODULE CREATION & PERSISTENCE ===")

# Dynamically create helper module file
# to demonstrate imports

module_code = '''"""Feature engineering and preprocessing utility module."""

__all__ = ["normalize_min_max", "impute_missing", "label_encode"]


def normalize_min_max(values):
    """Scales a list of numbers to [0, 1] range."""
    
    min_v = min(values)
    max_v = max(values)

    if min_v == max_v:
        return [0.0 for _ in values]

    return [
        round((v - min_v) / (max_v - min_v), 4)
        for v in values
    ]


def impute_missing(values, strategy="mean"):
    """Replaces None with column mean or mode."""

    valid_nums = [
        v for v in values
        if v is not None and isinstance(v, (int, float))
    ]

    if not valid_nums:
        return values

    fill_val = (
        round(sum(valid_nums) / len(valid_nums), 2)
        if strategy == "mean"
        else 0
    )

    return [
        fill_val if v is None else v
        for v in values
    ]


def label_encode(categories):
    """Maps distinct string labels to sequential integers."""

    unique = {
        cat: idx
        for idx, cat in enumerate(sorted(set(categories)))
    }

    return [unique[c] for c in categories]


def _internal_debug_helper():
    """Private utility helper (omitted from __all__)."""
    return "INTERNAL_STATE_OK"


if __name__ == "__main__":
    print("[Self-Test] Running data_prep internal test suite...")

    test_nums = [10, 20, 30]

    assert normalize_min_max(test_nums) == [
        0.0,
        0.5,
        1.0
    ], "Self-test failed"

    print("[Self-Test] All internal assertions passed.")
'''

module_filename = "data_prep.py"

with open(module_filename, "w", encoding="utf-8") as f:
    f.write(module_code)

print(f"Created module '{module_filename}' on disk.")


# ==========================================
# 4. IMPORTING THE CUSTOM MODULE
# ==========================================

print("\n=== 4. IMPORTING THE CUSTOM MODULE ===")

# Import newly created module
import data_prep

print(f"Imported Module: '{data_prep.__name__}'")
print(f"Documented: '{data_prep.__doc__}'")
print(
    "Exported symbols (__all__):",
    data_prep.__all__
)


# Test public functions

raw_scores = [
    12.0,
    None,
    45.0,
    None,
    80.0
]

clean_scores = data_prep.impute_missing(
    raw_scores,
    strategy="mean"
)

scaled_scores = data_prep.normalize_min_max(
    clean_scores
)

print("Original Scores:", raw_scores)
print("Imputed Scores: ", clean_scores)
print("Scaled Scores:  ", scaled_scores)


# ==========================================
# 5. MODULE CACHING & RELOADING
# ==========================================

print("\n=== 5. MODULE CACHING & RELOADING ===")

print(
    f"Is 'data_prep' in sys.modules?: "
    f"{'data_prep' in sys.modules}"
)

# Reload module using importlib

reloaded_module = importlib.reload(data_prep)

print(
    "Reloaded module identity check:",
    reloaded_module is data_prep
)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)


# ==========================================
# Q1 — Basic Module Creation
# ==========================================

# Creating a small inline converter module

with open(
    "temp_converter.py",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        'def fahrenheit_to_celsius(f): '
        'return round((f - 32) * 5 / 9, 2)\n'
    )

import temp_converter as tc

print(
    "Q1 Converted 98.6F to C:",
    tc.fahrenheit_to_celsius(98.6)
)


# ==========================================
# Q2 — The __name__ Inspection
# ==========================================

print(
    f"Q2 Current script executing as "
    f"__name__ = '{__name__}'"
)

print(
    f"   Imported module executing as "
    f"__name__ = '{data_prep.__name__}'"
)


# ==========================================
# Q3 — Inspecting sys.modules
# ==========================================

print(
    "Q3 'math' loaded in memory?:",
    "math" in sys.modules
)

print(
    "   'unloaded_module' loaded?:",
    "unloaded_module" in sys.modules
)


# ==========================================
# Q4 — Dynamic Path Injection
# ==========================================

custom_lib_dir = os.path.abspath("./custom_libs")

os.makedirs(
    custom_lib_dir,
    exist_ok=True
)

if custom_lib_dir not in sys.path:
    sys.path.append(custom_lib_dir)


with open(
    os.path.join(
        custom_lib_dir,
        "runtime_tool.py"
    ),
    "w",
    encoding="utf-8"
) as f:

    f.write(
        'def ping(): '
        'return "PONG from custom directory!"\n'
    )


import runtime_tool

print(
    "Q4 Dynamic path invocation:",
    runtime_tool.ping()
)


# ==========================================
# Q5 — Export Whitelist (__all__)
# ==========================================

print(
    "Q5 data_prep exported symbols via __all__:",
    data_prep.__all__
)

print(
    "   Is '_internal_debug_helper' in __all__?:",
    "_internal_debug_helper" in data_prep.__all__
)


# ==========================================
# Q6 — Module Introspection with dir()
# ==========================================

math_callables = [
    attr
    for attr in dir(math)
    if not attr.startswith("_")
    and callable(getattr(math, attr))
]

print(
    f"Q6 Callable math functions count: "
    f"{len(math_callables)} "
    f"(e.g., {math_callables[:5]})"
)


# ==========================================
# Q7 — In-Memory Reloading
# ==========================================

# Modify attribute in file, reload, verify

with open(
    "temp_converter.py",
    "a",
    encoding="utf-8"
) as f:

    f.write(
        "VERSION = 2.0\n"
    )


importlib.reload(tc)

print(
    "Q7 Reloaded module version:",
    getattr(tc, "VERSION", None)
)


# ==========================================
# Q8 — Avoiding Namespace Collision
# ==========================================

# Demonstrating separate module namespaces

import math
import cmath

real_sqrt = math.sqrt(25)
complex_sqrt = cmath.sqrt(-25)

print(
    f"Q8 math.sqrt(25): {real_sqrt} "
    f"vs cmath.sqrt(-25): {complex_sqrt}"
)


# ==========================================
# Q9 — Docstring Extraction
# ==========================================

print(
    "Q9 Extracted docstring from data_prep:"
)

print(
    "   ",
    data_prep.__doc__
)


# ==========================================
# Q10 — Challenge
# Modular Feature Engineering & Pipeline Engine
# ==========================================

class PipelineRunner:
    """Consumes the modular data_prep library
    to process tabular records.
    """

    def __init__(self, prep_module):
        self.prep = prep_module

    def process_records(self, raw_data: list[dict]):

        print(
            "\nQ10 Running Multi-Step "
            "Modular ETL Pipeline..."
        )

        # ----------------------------------
        # Extract columns
        # ----------------------------------

        ages = [
            row.get("age")
            for row in raw_data
        ]

        incomes = [
            row.get("income")
            for row in raw_data
        ]

        cities = [
            row.get("city", "Unknown")
            for row in raw_data
        ]

        # ----------------------------------
        # Step 1: Imputation via module
        # ----------------------------------

        clean_ages = self.prep.impute_missing(
            ages,
            strategy="mean"
        )

        clean_incomes = self.prep.impute_missing(
            incomes,
            strategy="mean"
        )

        # ----------------------------------
        # Step 2: Normalization via module
        # ----------------------------------

        scaled_ages = self.prep.normalize_min_max(
            clean_ages
        )

        scaled_incomes = self.prep.normalize_min_max(
            clean_incomes
        )

        # ----------------------------------
        # Step 3: Categorical encoding
        # ----------------------------------

        encoded_cities = self.prep.label_encode(
            cities
        )

        # ----------------------------------
        # Reconstruct tabular output
        # ----------------------------------

        processed_records = []

        for i in range(len(raw_data)):

            processed_records.append({
                "id": raw_data[i].get("id"),
                "norm_age": scaled_ages[i],
                "norm_income": scaled_incomes[i],
                "city_code": encoded_cities[i]
            })

        return processed_records


# ==========================================
# Q10 TEST DATA
# ==========================================

raw_customers = [

    {
        "id": "C101",
        "age": 25,
        "income": 50000,
        "city": "Bengaluru"
    },

    {
        "id": "C102",
        "age": None,
        "income": 80000,
        "city": "Mumbai"
    },

    {
        "id": "C103",
        "age": 45,
        "income": None,
        "city": "Bengaluru"
    },

    {
        "id": "C104",
        "age": 35,
        "income": 120000,
        "city": "Delhi"
    }
]


# ==========================================
# RUN PIPELINE
# ==========================================

pipeline = PipelineRunner(data_prep)

final_dataset = pipeline.process_records(
    raw_customers
)


# ==========================================
# DISPLAY FINAL DATASET
# ==========================================

print(
    "Q10 Final Engineered Features:"
)

for customer in final_dataset:
    print(
        "   ",
        customer
    )


# ==========================================
# CLEANUP TEMPORARY MODULE FILES
# ==========================================

print(
    "\n=== CLEANUP TEMPORARY MODULE FILES ==="
)


# ------------------------------------------
# Step 1: Remove custom directory from
# sys.path
# ------------------------------------------

if custom_lib_dir in sys.path:
    sys.path.remove(custom_lib_dir)


# ------------------------------------------
# Step 2: Remove temporary modules from
# Python's module cache
# ------------------------------------------

sys.modules.pop(
    "runtime_tool",
    None
)

sys.modules.pop(
    "temp_converter",
    None
)

sys.modules.pop(
    "data_prep",
    None
)


# ------------------------------------------
# Step 3: Delete temporary files
# ------------------------------------------

cleanup_files = [

    module_filename,

    "temp_converter.py",

    os.path.join(
        custom_lib_dir,
        "runtime_tool.py"
    )
]


for f_path in cleanup_files:

    if os.path.exists(f_path):

        try:

            os.remove(f_path)

            print(
                f"Deleted: {f_path}"
            )

        except PermissionError:

            print(
                f"Could not delete file: "
                f"{f_path}"
            )


# ------------------------------------------
# Step 4: Remove temporary directory
# ------------------------------------------

if os.path.exists(custom_lib_dir):

    try:

        os.rmdir(custom_lib_dir)

        print(
            f"Deleted directory: "
            f"{custom_lib_dir}"
        )

    except PermissionError:

        print(
            "Warning: Windows still has the "
            "directory locked."
        )

    except OSError as error:

        print(
            f"Could not remove directory: "
            f"{error}"
        )


print(
    "\nTemporary practice modules "
    "cleaned up successfully."
)

print(
    "\n=========================================="
)

print(
    "DAY 38 COMPLETED SUCCESSFULLY"
)

print(
    "=========================================="
)