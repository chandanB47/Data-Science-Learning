# ==========================================
# Day 28 — Python File Handling
# Script: file_handling.py
# ==========================================

from pathlib import Path
import os

print("=== 1. WRITING & APPENDING WITH CONTEXT MANAGER ===")
sample_path = Path("day28_sample.txt")

# Writing to a file (creates or overwrites)
with open(sample_path, "w", encoding="utf-8") as f:
    f.write("timestamp,level,event\n")
    f.write("2026-09-08 10:00:01,INFO,Service started\n")
    f.write("2026-09-08 10:00:05,WARNING,High memory usage\n")

print(f"File created at: {sample_path.resolve()}")

# Appending without truncating
with open(sample_path, "a", encoding="utf-8") as f:
    f.write("2026-09-08 10:00:12,ERROR,Database timeout\n")

print("Appended new log entry.")


print("\n=== 2. READING TECHNIQUES & STREAMING ===")
# Memory-efficient streaming iteration
print("Streaming line-by-line:")
with open(sample_path, "r", encoding="utf-8") as f:
    for line_idx, line in enumerate(f, start=1):
        print(f"  Line {line_idx}: {line.strip()}")


print("\n=== 3. FILE CURSOR CONTROL (TELL & SEEK) ===")
with open(sample_path, "r", encoding="utf-8") as f:
    print("Initial position:", f.tell())
    first_line = f.readline()
    print(f"Read line: {first_line.strip()!r}")
    print("Position after 1st line:", f.tell())
    
    # Seek back to start
    f.seek(0)
    print("Position after seek(0):", f.tell())
    reread_line = f.readline()
    print(f"Reread line: {reread_line.strip()!r}")


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Create and Write
def create_notes_file(filename, notes_list):
    with open(filename, "w", encoding="utf-8") as file:
        for note in notes_list:
            file.write(f"{note}\n")

notes_data = ["Clean dataset", "Train baseline model", "Evaluate precision-recall"]
create_notes_file("q1_notes.txt", notes_data)
print("Q1 Notes file created successfully.")


# Q2 — Line Counter
def count_lines(filename):
    total = 0
    with open(filename, "r", encoding="utf-8") as file:
        for _ in file:
            total += 1
    return total

print("Q2 Total lines in q1_notes.txt:", count_lines("q1_notes.txt"))


# Q3 — Keyword Line Filter
def filter_keyword_lines(source_file, dest_file, keyword):
    matched_count = 0
    with open(source_file, "r", encoding="utf-8") as src, open(dest_file, "w", encoding="utf-8") as dst:
        for line in src:
            if keyword in line:
                dst.write(line)
                matched_count += 1
    return matched_count

q3_matches = filter_keyword_lines(sample_path, "q3_errors.txt", "ERROR")
print(f"Q3 Filtered {q3_matches} error line(s) into q3_errors.txt.")


# Q4 — Word Frequency in File
def compute_word_frequency(filename):
    freq = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = "".join(c.lower() if c.isalnum() else " " for c in line)
            for word in cleaned_line.split():
                freq[word] = freq.get(word, 0) + 1
    return freq

print("Q4 Word Frequency in sample log:", compute_word_frequency(sample_path))


# Q5 — Safe File Appender
def safe_append(filename, text):
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"Cannot append to non-existent target: {filename}")
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{text}\n")

safe_append("q1_notes.txt", "Document experimental findings")
print("Q5 Successfully appended note to existing file.")
try:
    safe_append("non_existent_file.txt", "Should fail")
except FileNotFoundError as e:
    print("Q5 Caught expected error:", e)


# Q6 — Rewind and Reread
with open(sample_path, "r", encoding="utf-8") as file:
    chunk = file.read(20)
    pos = file.tell()
    file.seek(0)
    reset_line = file.readline().strip()

print(f"Q6 Read 20 bytes: {chunk!r} | Offset: {pos} | Reread from byte 0: {reset_line!r}")


# Q7 — Exclusive Creation ('x' mode)
def create_exclusive(filename):
    try:
        with open(filename, "x", encoding="utf-8") as file:
            file.write("Exclusive content.\n")
        return "Created successfully"
    except FileExistsError:
        return "File already exists. Aborted creation to prevent overwrite."

print("Q7 Attempt 1 (create):", create_exclusive("q7_exclusive.txt"))
print("Q7 Attempt 2 (collision):", create_exclusive("q7_exclusive.txt"))


# Q8 — Batch File Line Stripper
messy_lines = ["  Item 1  \n", "\n", "   \t\n", "Item 2\n", "  Item 3   \n"]
with open("q8_messy.txt", "w", encoding="utf-8") as file:
    file.writelines(messy_lines)

def clean_file_lines(src_file, dst_file):
    cleaned_count = 0
    with open(src_file, "r", encoding="utf-8") as src, open(dst_file, "w", encoding="utf-8") as dst:
        for line in src:
            stripped = line.strip()
            if stripped:
                dst.write(f"{stripped}\n")
                cleaned_count += 1
    return cleaned_count

cleaned_rows = clean_file_lines("q8_messy.txt", "q8_cleaned.txt")
print(f"Q8 Cleaned file created with {cleaned_rows} non-empty rows.")


# Q9 — Chunked File Reader
def read_in_chunks(file_obj, chunk_size=32):
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data

print("Q9 Streaming chunks of 32 characters:")
with open(sample_path, "r", encoding="utf-8") as file:
    for idx, chunk_data in enumerate(read_in_chunks(file, chunk_size=32), start=1):
        print(f"   Chunk {idx} [{len(chunk_data)} chars]: {chunk_data!r}")


# Q10 — Challenge 🔥 (Log Metric Extractor & Summary Report Generator)
simulated_logs = [
    "2026-09-08 10:15:30 GET /api/v1/users 200 120ms\n",
    "2026-09-08 10:15:32 POST /api/v1/auth 200 240ms\n",
    "2026-09-08 10:15:35 GET /api/v1/dataset 404 45ms\n",
    "2026-09-08 10:15:38 GET /api/v1/records 500 510ms\n",
    "2026-09-08 10:15:40 GET /api/v1/users 200 115ms\n",
]

log_filepath = "access.log"
with open(log_filepath, "w", encoding="utf-8") as file:
    file.writelines(simulated_logs)

def parse_server_log(log_path, report_path):
    total_requests = 0
    status_200 = 0
    status_errors = 0
    total_latency = 0.0

    with open(log_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            parts = line.strip().split()
            if len(parts) >= 6:
                total_requests += 1
                status_code = int(parts[4])
                latency = float(parts[5].replace("ms", ""))

                if status_code == 200:
                    status_200 += 1
                elif status_code >= 400:
                    status_errors += 1

                total_latency += latency

    avg_latency = round(total_latency / total_requests, 2) if total_requests else 0.0

    # Write summary report
    with open(report_path, "w", encoding="utf-8") as rep:
        rep.write("=== LOG ANALYSIS SUMMARY REPORT ===\n")
        rep.write(f"Total Requests:       {total_requests}\n")
        rep.write(f"Successful (200 OK):  {status_200}\n")
        rep.write(f"Errors (4xx / 5xx):   {status_errors}\n")
        rep.write(f"Average Latency:      {avg_latency} ms\n")

    return total_requests, status_200, status_errors, avg_latency

reqs, succ, errs, avg_lat = parse_server_log(log_filepath, "report.txt")

print("\nQ10 Log Analysis Complete:")
print(f"   Processed {reqs} requests | Success: {succ} | Errors: {errs} | Avg Latency: {avg_lat} ms")
print("   Summary written to 'report.txt'.")

# Cleanup created temporary files
cleanup_targets = [
    "day28_sample.txt", "q1_notes.txt", "q3_errors.txt",
    "q7_exclusive.txt", "q8_messy.txt", "q8_cleaned.txt",
    "access.log", "report.txt"
]
for target in cleanup_targets:
    if os.path.exists(target):
        os.remove(target)
print("\nTemporary practice files cleaned up.")




















