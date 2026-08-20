# ==========================================
# Day 15 — Python Strings Advanced
# Script: strings_advanced.py
# ==========================================

print("=== 1. ADVANCED SLICING & REVERSING ===")
text = "DataScience2026"
print("Every 2nd char:", text[::2])
print("Reversed:", text[::-1])
print("Sub-slice [-4:]:", text[-4:])


print("\n=== 2. WHITESPACE & CHARACTER STRIPPING ===")
raw_input = "  ###User_101###  \n"
cleaned = raw_input.strip().strip("#")
print("Raw:", repr(raw_input))
print("Cleaned:", cleaned)


print("\n=== 3. SPLIT AND JOIN ===")
csv_row = "2026-08-20,Production,Error,500"
tokens = csv_row.split(",")
print("Tokens:", tokens)

file_path = "/".join(["var", "log", "nginx", "access.log"])
print("Joined Path:", file_path)


print("\n=== 4. SEARCHING & VALIDATION ===")
log = "ERROR: Failed database connection"
print("Starts with ERROR/CRITICAL:", log.startswith(("ERROR", "CRITICAL")))
print("Find 'database': index", log.find("database"))
print("Count of 'e':", log.count("e"))


print("\n=== 5. F-STRINGS & FORMAT SPECIFIERS ===")
metric = "accuracy"
score = 0.945821
total_records = 1500000
formatted = f"Metric: {metric.upper():<10} | Score: {score:.2%} | Records: {total_records:,}"
print(formatted)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Palindrome Verifier
word_q1 = "RaceCar"
is_palindrome = word_q1.lower() == word_q1.lower()[::-1]
print(f"Q1 Is '{word_q1}' a palindrome?:", is_palindrome)


# Q2 — Domain Extractor
email_q2 = "student_analytics@datacompany.org"
domain = email_q2.split("@")[-1]
print("Q2 Extracted Domain:", domain)


# Q3 — Title Sanitization
raw_title = "___data_science_and_mAchine_leArning___"
clean_title = raw_title.strip("_").replace("_", " ").title()
print("Q3 Sanitized Title:", clean_title)


# Q4 — Substring Frequency
doc_q4 = "The quick brown fox jumps over the lazy dog. THE FOX was clever."
fox_count = doc_q4.lower().count("fox")
print("Q4 Count of 'fox':", fox_count)


# Q5 — File Extension Filter
filename = "annual_report_2026.pdf"
is_valid_ext = filename.endswith((".pdf", ".docx", ".xlsx"))
print("Q5 Valid Extension?:", is_valid_ext)


# Q6 — Sensitive Data Masking
card_number = "4532891044238819"
masked_card = f"{'*' * (len(card_number) - 4)}{card_number[-4:]}"
print("Q6 Masked Card:", masked_card)


# Q7 — URL Slug Generator
title_q7 = "10 Tips For Clean Code In 2026!"
slug = "-".join([
    "".join(c for c in word if c.isalnum()).lower()
    for word in title_q7.split()
    if any(c.isalnum() for c in word)
])
print("Q7 URL Slug:", slug)


# Q8 — Prefix & Suffix Stripping
endpoint = "https://api.github.com/v1"
clean_endpoint = endpoint.removeprefix("https://").removesuffix("/v1")
print("Q8 Clean Endpoint:", clean_endpoint)


# Q9 — Extract and Sum Digits
order_summary = "Items: 12 books, 4 pens, 100 markers, 2 notebooks"
total_quantity = sum(int(tok) for tok in order_summary.replace(",", "").split() if tok.isdigit())
print("Q9 Total Quantity:", total_quantity)


# Q10 — Challenge 🔥 (Log Parser)
log_entry = "[2026-08-20 14:32:01] [CRITICAL] [IP: 192.168.1.105] - Database connection pool exhausted"

parts = log_entry.split(" - ")
metadata_tags = [tag.strip("[]") for tag in parts[0].split("] [")]

parsed_log = {
    "timestamp": metadata_tags[0],
    "level": metadata_tags[1],
    "ip": metadata_tags[2].removeprefix("IP: "),
    "message": parts[1]
}
print("Q10 Parsed Log Record:\n", parsed_log)













