# STEP 2: FUNCTIONS WITH PARAMETERS (INPUT)
# ============================================================================

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob") 
greet_person("Kavya")   # Output: Hello, Bob!

# ============================================================================

def add_numbers(a, b):
    """Function with multiple parameters"""
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # Output: 5 + 3 = 8
add_numbers(10, 20)  # Output: 10 + 20 = 30



