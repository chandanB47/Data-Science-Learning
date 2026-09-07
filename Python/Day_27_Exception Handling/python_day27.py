# ==========================================
# Day 27 — Python Exception Handling
# Script: exception_handling.py
# ==========================================

print("=== 1. TRY - EXCEPT - ELSE - FINALLY ===")
def divide_records(total_items, batch_size):
    try:
        batches = total_items / batch_size
    except ZeroDivisionError as e:
        print(f"[EXCEPT] Caught calculation error: {e}")
        return 0
    else:
        print("[ELSE] Batch calculation executed successfully.")
        return batches
    finally:
        print("[FINALLY] Resource check and execution logged.")

print("Run 1 (Valid):", divide_records(100, 20))
print("\nRun 2 (Invalid):", divide_records(100, 0))


print("\n=== 2. CATCHING MULTIPLE SPECIFIC EXCEPTIONS ===")
def parse_payload_element(payload, key, index):
    try:
        target_list = payload[key]
        item = target_list[index]
        return int(item)
    except KeyError:
        print(f"[ERROR] Key '{key}' not found in payload.")
    except IndexError:
        print(f"[ERROR] Index {index} is out of range.")
    except (ValueError, TypeError) as err:
        print(f"[ERROR] Conversion failed: {err}")
    return None

data_blob = {"scores": ["98", "invalid", "100"]}
print("Result A:", parse_payload_element(data_blob, "scores", 0))
print("Result B:", parse_payload_element(data_blob, "metrics", 0))
print("Result C:", parse_payload_element(data_blob, "scores", 10))
print("Result D:", parse_payload_element(data_blob, "scores", 1))


print("\n=== 3. CUSTOM DOMAIN EXCEPTIONS ===")
class SchemaValidationError(Exception):
    """Raised when an ingested record violates dataset schema constraints."""
    pass

def register_user(username, age):
    if not username:
        raise SchemaValidationError("Username cannot be empty.")
    if age < 18:
        raise SchemaValidationError(f"User '{username}' is underage ({age}).")
    return {"user": username, "status": "REGISTERED"}

try:
    print(register_user("Alice", 25))
    print(register_user("Bob", 15))
except SchemaValidationError as err:
    print(f"[VALIDATION FAILED] {err}")


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Safe Integer Parser
def safe_int(val, default=0):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

print("Q1 safe_int('123'):", safe_int("123"))
print("Q1 safe_int('corrupt', default=-1):", safe_int("corrupt", default=-1))
print("Q1 safe_int(None):", safe_int(None))


# Q2 — Zero Division Guard
def calc_pct_change(old_val, new_val):
    try:
        change = ((new_val - old_val) / old_val) * 100
        return round(change, 2)
    except ZeroDivisionError:
        return 0.0

print("Q2 Pct Change (100 -> 150):", calc_pct_change(100, 150))
print("Q2 Pct Change (0 -> 50):", calc_pct_change(0, 50))


# Q3 — Dictionary Key Fallback with Custom Exception
class MissingUserField(Exception):
    pass

def extract_user_credentials(user_dict):
    try:
        return user_dict["user_id"], user_dict["email"]
    except KeyError as missing_key:
        raise MissingUserField(f"Missing mandatory user credential: {missing_key}")

try:
    extract_user_credentials({"user_id": 101})
except MissingUserField as err:
    print("Q3 Caught custom error:", err)


# Q4 — Resource Cleanup Simulator
def database_query_simulation(fail=False):
    print("   [DB] Connection opened.")
    try:
        if fail:
            raise ConnectionResetError("Connection lost during query.")
        print("   [DB] Query processed successfully.")
    finally:
        print("   [DB] Connection closed reliably.")

print("Q4 Successful Query:")
database_query_simulation(fail=False)
print("Q4 Failed Query:")
try:
    database_query_simulation(fail=True)
except ConnectionResetError as err:
    print("   Handled upstream:", err)


# Q5 — Multiple Exception Tuple
def inspect_nested(seq, index, key):
    try:
        return seq[index][key]
    except (KeyError, IndexError, TypeError) as err:
        return f"Extraction failed ({type(err).__name__})"

print("Q5 Good:", inspect_nested([{"title": "Intro"}], 0, "title"))
print("Q5 Index issue:", inspect_nested([], 0, "title"))
print("Q5 Key issue:", inspect_nested([{"title": "Intro"}], 0, "author"))


# Q6 — Reraising Exceptions
def transform_metric(val):
    try:
        return float(val) ** 2
    except ValueError as err:
        print("   [LOG] Intercepted invalid metric, forwarding up stack...")
        raise

try:
    print("Q6 Result:", transform_metric("valid_10"))
except ValueError:
    print("Q6 Caught reraised exception at caller level.")


# Q7 — Validating Function Input Bounds
def set_learning_rate(lr):
    if not (0.0 < lr < 1.0):
        raise ValueError(f"Learning rate must be strictly between 0.0 and 1.0. Given: {lr}")
    return f"Learning rate set to {lr}"

print("Q7 LR valid:", set_learning_rate(0.01))
try:
    set_learning_rate(1.5)
except ValueError as err:
    print("Q7 LR invalid handled:", err)


# Q8 — Custom NegativeValueException
class NegativeBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise NegativeBalanceError(f"Insufficient funds: withdrawal of ${amount} exceeds balance ${balance}.")
    return balance - amount

try:
    withdraw(100, 250)
except NegativeBalanceError as err:
    print("Q8 Withdrawal error:", err)


# Q9 — Safe List Mean Calculation
def safe_mean(numbers):
    try:
        return round(sum(numbers) / len(numbers), 2)
    except ZeroDivisionError:
        return 0.0
    except TypeError:
        return None

print("Q9 Valid mean:", safe_mean([10, 20, 30]))
print("Q9 Empty list mean:", safe_mean([]))
print("Q9 Corrupted list mean:", safe_mean([10, "twenty", 30]))


# Q10 — Challenge 🔥 (Batch Ingestion Audit Pipeline)
class NegativeAmountError(Exception):
    pass

def ingest_transaction_batch(raw_batch):
    valid_records = []
    corrupted_records = []

    for item in raw_batch:
        try:
            # 1. Check mandatory fields
            if "tx_id" not in item:
                raise KeyError("Missing 'tx_id' identifier")
            if "amount" not in item:
                raise KeyError("Missing 'amount' value")
            
            # 2. Type cast and validate bounds
            amount_val = float(item["amount"])
            if amount_val < 0:
                raise NegativeAmountError(f"Negative transaction amount ({amount_val})")
            
            # Record valid entry
            valid_records.append({"tx_id": item["tx_id"], "amount": amount_val})
            
        except (KeyError, ValueError, NegativeAmountError) as err:
            corrupted_records.append({
                "raw_item": item,
                "error_type": type(err).__name__,
                "reason": str(err)
            })

    return valid_records, corrupted_records

raw_tx_batch = [
    {"tx_id": "T1", "amount": "150.50"},
    {"tx_id": "T2", "amount": "-20.00"},
    {"tx_id": "T3"},
    {"amount": "80.00"},
    {"tx_id": "T5", "amount": "N/A"},
    {"tx_id": "T6", "amount": "450.00"}
]

valid_txs, invalid_txs = ingest_transaction_batch(raw_tx_batch)

print("Q10 Ingestion Audit Summary:")
print(f"   Valid Records Ingested: {len(valid_txs)}")
for v in valid_txs:
    print("    ", v)

print(f"   Corrupted Records Flagged: {len(invalid_txs)}")
for inv in invalid_txs:
    print("    ", inv)



    