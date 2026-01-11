"""
PYTHON FUNCTIONS - STEP BY STEP GUIDE
=====================================

A function is a reusable block of code that performs a specific task.
Functions help us avoid code repetition and make our code more organized.
"""

# ============================================================================
# STEP 1: BASIC FUNCTION SYNTAX
# ============================================================================

def greet():
    """Simple function without parameters"""
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!


# ============================================================================
# STEP 2: FUNCTIONS WITH PARAMETERS (INPUT)
# ============================================================================

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!


def add_numbers(a, b):
    """Function with multiple parameters"""
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # Output: 5 + 3 = 8
add_numbers(10, 20)  # Output: 10 + 20 = 30


# ============================================================================
# STEP 3: RETURN VALUES (OUTPUT)
# ============================================================================

def multiply(x, y):
    """Function that returns a value"""
    return x * y

result = multiply(4, 5)
print(f"Result: {result}")  # Output: Result: 20

# You can use the return value directly
print(f"10 * 3 = {multiply(10, 3)}")  # Output: 10 * 3 = 30


def get_full_name(first_name, last_name):
    """Function returning a string"""
    return f"{first_name} {last_name}"

full_name = get_full_name("John", "Doe")
print(full_name)  # Output: John Doe


# ============================================================================
# STEP 4: DEFAULT PARAMETERS
# ============================================================================

def greet_with_default(name="Guest"):
    """Function with default parameter value"""
    print(f"Hello, {name}!")

greet_with_default()  # Output: Hello, Guest! (uses default)
greet_with_default("Alice")  # Output: Hello, Alice! (overrides default)


def calculate_total(price, tax_rate=0.10, discount=0):
    """Function with multiple default parameters"""
    subtotal = price - discount
    total = subtotal * (1 + tax_rate)
    return total

print(f"Total: ${calculate_total(100):.2f}")  # Uses default tax_rate and discount
print(f"Total: ${calculate_total(100, 0.15):.2f}")  # Uses custom tax_rate
print(f"Total: ${calculate_total(100, 0.15, 10):.2f}")  # Uses all custom values


# ============================================================================
# STEP 5: KEYWORD ARGUMENTS (NAMED ARGUMENTS)
# ============================================================================

def create_profile(name, age, city, occupation):
    """Function demonstrating keyword arguments"""
    print(f"Name: {name}, Age: {age}, City: {city}, Occupation: {occupation}")

# Positional arguments (order matters)
create_profile("Alice", 25, "New York", "Engineer")

# Keyword arguments (order doesn't matter)
create_profile(name="Bob", occupation="Teacher", age=30, city="London")

# Mixed (positional first, then keyword)
create_profile("Charlie", 28, occupation="Doctor", city="Boston")


# ============================================================================
# STEP 6: RETURN MULTIPLE VALUES
# ============================================================================

def calculate_stats(numbers):
    """Function returning multiple values (as a tuple)"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    maximum = max(numbers) if numbers else 0
    minimum = min(numbers) if numbers else 0
    return total, count, average, maximum, minimum

stats = calculate_stats([10, 20, 30, 40, 50])
print(f"Stats: {stats}")  # Output: Stats: (150, 5, 30.0, 50, 10)

# Unpacking multiple return values
total, count, avg, max_val, min_val = calculate_stats([5, 15, 25])
print(f"Total: {total}, Count: {count}, Average: {avg:.2f}")
print(f"Max: {max_val}, Min: {min_val}")


# ============================================================================
# STEP 7: VARIABLE NUMBER OF ARGUMENTS (*args)
# ============================================================================

def sum_all(*args):
    """Function that accepts any number of arguments"""
    total = 0
    for number in args:
        total += number
    return total

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(10, 20, 30, 40, 50))  # Output: 150
print(sum_all(5))  # Output: 5
print(sum_all())  # Output: 0


def make_pizza(*toppings):
    """Function demonstrating *args with a practical example"""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# ============================================================================
# STEP 8: KEYWORD ARGUMENTS (**kwargs)
# ============================================================================

def create_user(**kwargs):
    """Function that accepts any number of keyword arguments"""
    print("User details:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_user(name="Alice", age=25, email="alice@example.com")
create_user(name="Bob", city="New York", occupation="Engineer", salary=75000)


def process_order(item, quantity, **options):
    """Function combining regular parameters with **kwargs"""
    print(f"Order: {quantity} x {item}")
    if options:
        print("Options:")
        for key, value in options.items():
            print(f"  {key}: {value}")

process_order("Pizza", 2, size="Large", crust="Thin", extra_cheese=True)


# ============================================================================
# STEP 9: DOCSTRINGS (FUNCTION DOCUMENTATION)
# ============================================================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle (length * width)
    
    Example:
    >>> calculate_area(5, 3)
    15
    """
    return length * width

# Access the docstring
print(calculate_area.__doc__)
print(f"Area: {calculate_area(5, 3)}")


# ============================================================================
# STEP 10: VARIABLE SCOPE
# ============================================================================

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    """Demonstrating local vs global scope"""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

demonstrate_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error - local_var doesn't exist here


def modify_global():
    """Modifying global variable (use with caution)"""
    global global_var
    global_var = "Modified global"
    print(f"Inside function: {global_var}")

print(f"Before: {global_var}")
modify_global()
print(f"After: {global_var}")


# ============================================================================
# STEP 11: PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")


# Example 2: Password checker
def check_password(password, min_length=8):
    """Check if password meets requirements"""
    if len(password) < min_length:
        return False, f"Password must be at least {min_length} characters"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number"
    if not any(char.isalpha() for char in password):
        return False, "Password must contain at least one letter"
    return True, "Password is valid"

is_valid, message = check_password("mypassword123")
print(f"Password check: {message}")

is_valid, message = check_password("short")
print(f"Password check: {message}")


# Example 3: Shopping cart calculator
def calculate_cart_total(items, tax_rate=0.08, shipping=5.00):
    """
    Calculate total cost of shopping cart
    
    items: list of tuples (item_name, price)
    tax_rate: tax rate as decimal (default 0.08 = 8%)
    shipping: shipping cost (default $5.00)
    """
    subtotal = sum(price for _, price in items)
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping
    
    return {
        'subtotal': subtotal,
        'tax': tax,
        'shipping': shipping,
        'total': total
    }

cart = [
    ("Laptop", 999.99),
    ("Mouse", 29.99),
    ("Keyboard", 79.99)
]

receipt = calculate_cart_total(cart)
print("\nShopping Cart Receipt:")
print(f"Subtotal: ${receipt['subtotal']:.2f}")
print(f"Tax: ${receipt['tax']:.2f}")
print(f"Shipping: ${receipt['shipping']:.2f}")
print(f"Total: ${receipt['total']:.2f}")


# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
"""
1. Functions are defined using the 'def' keyword
2. Functions can accept parameters (inputs)
3. Functions can return values using 'return'
4. Default parameters have default values if not provided
5. Keyword arguments allow passing arguments by name
6. *args allows variable number of positional arguments
7. **kwargs allows variable number of keyword arguments
8. Functions can return multiple values (as tuples)
9. Docstrings document what functions do
10. Variables have scope (global vs local)
"""

