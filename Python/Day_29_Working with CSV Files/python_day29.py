# ==========================================
# Day 29 — Python CSV Files
# Script: csv_files.py
# ==========================================

import csv
from pathlib import Path
import os

print("=== 1. WRITING & READING WITH CSV.READER / CSV.WRITER ===")
sample_csv_path = Path("day29_transactions.csv")

# Writing standard tabular rows
headers = ["tx_id", "customer", "amount", "city"]
rows = [
    ["T1001", "Meera", "250.75", "Bengaluru"],
    ["T1002", "Alex", "120.00", "New York, NY"],  # Contains a comma in the string
    ["T1003", "Karan", "850.50", "Mumbai"]
]

with open(sample_csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("File written successfully.")

# Reading using csv.reader
print("\nReading with csv.reader:")
with open(sample_csv_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Advance iterator to skip/capture header
    print("Header:", header_row)
    for r in reader:
        print("  Row:", r)


print("\n=== 2. USING CSV.DICTREADER & CSV.DICTWRITER ===")
dict_csv_path = Path("day29_employees.csv")
emp_fields = ["emp_id", "name", "department", "salary", "status"]
emp_data = [
    {"emp_id": "E101", "name": "Aman", "department": "Analytics", "salary": "75000", "status": "Active"},
    {"emp_id": "E102", "name": "Priya", "department": "Engineering", "salary": "95000", "status": "Active"},
    {"emp_id": "E103", "name": "Rohan", "department": "Marketing", "salary": "52000", "status": "Inactive"},
    {"emp_id": "E104", "name": "Sara", "department": "Analytics", "salary": "82000", "status": "Active"}
]

# Writing using DictWriter
with open(dict_csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=emp_fields)
    writer.writeheader()
    writer.writerows(emp_data)

# Reading using DictReader
print("Reading with csv.DictReader:")
with open(dict_csv_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for emp in reader:
        print(f"  {emp['name']} | Dept: {emp['department']} | Salary: ${emp['salary']}")


print("\n=== 3. CUSTOM DELIMITERS (TSV FORMAT) ===")
tsv_path = Path("day29_metrics.tsv")
with open(tsv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["epoch", "loss", "accuracy"])
    writer.writerow([1, 0.65, 0.72])
    writer.writerow([2, 0.42, 0.88])

with open(tsv_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print("  TSV Row:", row)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Row Counter
def count_csv_rows(filepath):
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        return sum(1 for _ in reader)

print("Q1 Total data rows in transactions:", count_csv_rows(sample_csv_path))


# Q2 — Header Extractor
def get_csv_headers(filepath):
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return next(reader, [])

print("Q2 Extracted Headers:", get_csv_headers(sample_csv_path))


# Q3 — Column Extractor
def extract_column(filepath, column_name):
    column_values = []
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if column_name in row:
                column_values.append(row[column_name])
    return column_values

print("Q3 Extracted 'city' column:", extract_column(sample_csv_path, "city"))


# Q4 — Tab-Separated Exporter
def convert_csv_to_tsv(source_csv, output_tsv):
    with open(source_csv, "r", newline="", encoding="utf-8") as src, \
         open(output_tsv, "w", newline="", encoding="utf-8") as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst, delimiter="\t")
        for row in reader:
            writer.writerow(row)

convert_csv_to_tsv(sample_csv_path, "q4_converted.tsv")
print("Q4 Successfully converted CSV to TSV.")


# Q5 — Row Appender
def append_csv_record(filepath, fieldnames, record_dict):
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(record_dict)

new_employee = {"emp_id": "E105", "name": "Kavita", "department": "Design", "salary": "71000", "status": "Active"}
append_csv_record(dict_csv_path, emp_fields, new_employee)
print("Q5 Appended record E105 to employees CSV.")


# Q6 — Numeric Column Aggregator
def aggregate_column(filepath, numeric_column):
    total = 0.0
    count = 0
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                val = float(row[numeric_column])
                total += val
                count += 1
            except (ValueError, KeyError):
                continue
    avg = round(total / count, 2) if count else 0.0
    return round(total, 2), avg

total_sal, avg_sal = aggregate_column(dict_csv_path, "salary")
print(f"Q6 Salary Aggregation: Total = ${total_sal:,} \vert Average =${avg_sal:,}")


# Q7 — Handling Quoted Fields
quoted_path = "q7_addresses.csv"
records_with_commas = [
    ["name", "full_address"],
    ["Company HQ", "100 Tech Park, Building A, Bengaluru"],
    ["Branch Office", "Suite 404, 5th Avenue, New York, NY"]
]
with open(quoted_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(records_with_commas)

with open(quoted_path, "r", newline="", encoding="utf-8") as f:
    print("Q7 Verification of Quoted CSV:")
    for raw_line in f:
        print("  ", raw_line.strip())


# Q8 — Dynamic Header Renamer
dirty_header_file = "q8_raw.csv"
with open(dirty_header_file, "w", newline="", encoding="utf-8") as f:
    f.write("User Id,First Name,Account Balance\n101,Aman,500.0\n")

def sanitize_csv_headers(src_file, dst_file):
    with open(src_file, "r", newline="", encoding="utf-8") as src, \
         open(dst_file, "w", newline="", encoding="utf-8") as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst)
        raw_headers = next(reader)
        clean_headers = [h.strip().lower().replace(" ", "_") for h in raw_headers]
        writer.writerow(clean_headers)
        for row in reader:
            writer.writerow(row)

sanitize_csv_headers(dirty_header_file, "q8_cleaned.csv")
print("Q8 Sanitized headers:", get_csv_headers("q8_cleaned.csv"))


# Q9 — Missing Value Imputer
unimputed_file = "q9_missing.csv"
with open(unimputed_file, "w", newline="", encoding="utf-8") as f:
    f.write("id,score\n1,85\n2,\n3,92\n4,\n")

def impute_missing_csv_values(src_file, dst_file, fallback_val="0"):
    with open(src_file, "r", newline="", encoding="utf-8") as src, \
         open(dst_file, "w", newline="", encoding="utf-8") as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst)
        writer.writerow(next(reader))  # copy headers
        for row in reader:
            clean_row = [val if val.strip() != "" else fallback_val for val in row]
            writer.writerow(clean_row)

impute_missing_csv_values(unimputed_file, "q9_imputed.csv")
print("Q9 Imputed Data Content:")
with open("q9_imputed.csv", "r", newline="", encoding="utf-8") as f:
    for line in f:
        print("  ", line.strip())


# Q10 — Challenge 🔥 (CSV ETL Pipeline & Filter)
def etl_employee_pipeline(input_csv, output_csv):
    output_fields = ["emp_id", "name", "department", "salary", "tax_bracket"]
    processed_count = 0

    with open(input_csv, "r", newline="", encoding="utf-8") as src, \
         open(output_csv, "w", newline="", encoding="utf-8") as dst:
        reader = csv.DictReader(src)
        writer = csv.DictWriter(dst, fieldnames=output_fields)
        writer.writeheader()

        for row in reader:
            status = row.get("status", "").strip()
            try:
                salary = float(row.get("salary", 0))
            except ValueError:
                continue

            # Filtering condition
            if status == "Active" and salary >= 60000:
                # Column transformation / enrichment
                tax_bracket = "High" if salary >= 80000 else "Medium"
                
                writer.writerow({
                    "emp_id": row["emp_id"],
                    "name": row["name"],
                    "department": row["department"],
                    "salary": f"{salary:.2f}",
                    "tax_bracket": tax_bracket
                })
                processed_count += 1

    return processed_count

filtered_output_path = "q10_filtered_employees.csv"
qualified_count = etl_employee_pipeline(dict_csv_path, filtered_output_path)

print(f"\nQ10 ETL Complete: Exported {qualified_count} qualified employees to '{filtered_output_path}':")
with open(filtered_output_path, "r", newline="", encoding="utf-8") as f:
    for line in f:
        print("  ", line.strip())

# Clean up temporary practice files
cleanup_files = [
    sample_csv_path, dict_csv_path, tsv_path, "q4_converted.tsv",
    quoted_path, dirty_header_file, "q8_cleaned.csv",
    unimputed_file, "q9_imputed.csv", filtered_output_path
]
for f_path in cleanup_files:
    if os.path.exists(f_path):
        os.remove(f_path)
print("\nTemporary practice CSV files cleaned up.")




