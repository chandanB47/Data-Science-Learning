# ==========================================
# Day 22 — Python *args and **kwargs
# Script: args_and_kwargs.py
# ==========================================

print("=== 1. POSITIONAL PACKING (*ARGS) ===")
def sum_all(*numbers):
    print(f"Received tuple: {numbers} (Length: {len(numbers)})")
    return sum(numbers)

print("Sum:", sum_all(10, 20, 30, 40))
print("Sum empty:", sum_all())


print("\n=== 2. KEYWORD PACKING (**KWARGS) ===")
def configure_pipeline(**options):
    print("Received options dictionary:", options)
    for key, value in options.items():
        print(f"  - Config: {key} -> {value}")

configure_pipeline(learning_rate=0.01, epochs=50, optimizer="adam")


print("\n=== 3. CALL-TIME UNPACKING (* AND **) ===")
def display_training_run(model, epochs, lr):
    return f"Model: {model} | Epochs: {epochs} | LR: {lr}"

args_list = ["ResNet", 100]
kwargs_dict = {"lr": 0.001}

# Combining positional unpack (*) and keyword unpack (**)
print(display_training_run(*args_list, **kwargs_dict))


print("\n=== 4. CANONICAL PARAMETER ORDERING ===")
def audit_stage(stage_name, *flags, mode="strict", **metadata):
    return {
        "stage": stage_name,
        "flags": flags,
        "mode": mode,
        "metadata": metadata
    }

audit_info = audit_stage(
    "Data_Ingestion",
    "FLAG_SKIP_HEADER", "FLAG_UTF8",
    mode="permissive",
    source="S3_Bucket", records=150000
)
print("Audit Output:\n", audit_info)


print("\n=== 5. ARGUMENT FORWARDING & WRAPPER ===")
def core_compute(base, multiplier=1):
    return base * multiplier

def logged_compute(*args, **kwargs):
    print(f"[TRACE] Invoking core_compute with args={args}, kwargs={kwargs}")
    result = core_compute(*args, **kwargs)
    print(f"[TRACE] Computation finished: {result}")
    return result

logged_compute(50, multiplier=3)




