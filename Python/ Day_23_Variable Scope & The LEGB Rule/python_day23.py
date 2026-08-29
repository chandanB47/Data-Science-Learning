# ==========================================
# Day 23 — Variable Scope & LEGB
# Script: scope_legb.py
# ==========================================

print("=== 1. THE LEGB RESOLUTION DEMO ===")
level = "GLOBAL"

def outer_function():
    level = "ENCLOSING"
    
    def inner_function():
        level = "LOCAL"
        return f"Resolved level: {level}"
    
    return inner_function()

print(outer_function())


print("\n=== 2. GLOBAL VARIABLE MUTATION ===")
pipeline_runs = 0

def execute_pipeline():
    global pipeline_runs
    pipeline_runs += 1
    print(f"[PIPELINE] Execution #{pipeline_runs} completed.")

execute_pipeline()
execute_pipeline()
print("Global Total Runs:", pipeline_runs)


print("\n=== 3. CLOSURES WITH NONLOCAL ===")
def create_accumulator(initial_value=0):
    total = initial_value
    
    def add(value):
        nonlocal total
        total += value
        return total
    
    return add

acc_a = create_accumulator(10)
print("Accumulator A (+5):", acc_a(5))
print("Accumulator A (+20):", acc_a(20))

acc_b = create_accumulator(100)
print("Accumulator B (+1):", acc_b(1))


print("\n=== 4. DATA TRANSFORMER FACTORY ===")
def make_min_max_scaler(min_val, max_val):
    """Enclosing scope captures normalization bounds."""
    range_span = max_val - min_val
    
    def scale(x):
        return round((x - min_val) / range_span, 4)
    
    return scale

scaler_0_100 = make_min_max_scaler(0, 100)
print("Scaled 75 (0-100 scale):", scaler_0_100(75))
print("Scaled 25 (0-100 scale):", scaler_0_100(25))


