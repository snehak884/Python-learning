"""
PRACTICAL EXAMPLE: Using External Modules Step by Step
=======================================================

This file demonstrates how to use external modules in practice.
Some examples require installation first.
"""

# ============================================================================
# EXAMPLE 1: Using 'requests' module (HTTP requests)
# ============================================================================

"""
STEP 1: Install requests in terminal:
   pip install requests

STEP 2: Import it in your code
STEP 3: Use it
"""

# Uncomment the code below after installing requests:
# import requests
#
# print("=== Example 1: Using requests module ===")
# 
# # Make a GET request to an API
# response = requests.get('https://api.github.com')
# 
# print(f"Status Code: {response.status_code}")
# print(f"Status: {'Success' if response.status_code == 200 else 'Error'}")
# print(f"Content Type: {response.headers.get('content-type')}")
# print()


# ============================================================================
# EXAMPLE 2: Using 'datetime' with external formatting (built-in)
# ============================================================================

from datetime import datetime

print("=== Example 2: Using datetime module (built-in) ===")

now = datetime.now()
print(f"Current Date and Time: {now}")
print(f"Formatted: {now.strftime('%B %d, %Y at %I:%M %p')}")
print()


# ============================================================================
# EXAMPLE 3: Complete workflow - Installing and using an external module
# ============================================================================

"""
COMPLETE WORKFLOW EXAMPLE:

1. Open terminal/command prompt
2. Navigate to your project directory
3. Install the module:
   
   pip install requests
   
   OR if you need to specify Python 3:
   
   pip3 install requests

4. Verify installation:
   
   pip list
   
   OR
   
   pip show requests

5. Create a Python file and import it:
   
   import requests

6. Use it in your code:
   
   response = requests.get('https://example.com')
   print(response.status_code)
"""


# ============================================================================
# EXAMPLE 4: Creating requirements.txt
# ============================================================================

"""
To create a requirements.txt file:

1. Create a file named 'requirements.txt' in your project root
2. List all your dependencies:

   requests==2.28.0
   numpy==1.23.0
   pandas==1.5.0

3. Install all dependencies at once:
   
   pip install -r requirements.txt

4. Or generate requirements.txt from installed packages:
   
   pip freeze > requirements.txt
"""


# ============================================================================
# EXAMPLE 5: Checking if a module is installed
# ============================================================================

print("=== Example 5: Checking module installation ===")

# Try to import a built-in module (always available)
try:
    import math
    print("✓ math module is available (built-in)")
except ImportError:
    print("✗ math module not found")

# Try to import an external module
try:
    import requests
    print("✓ requests module is installed")
    print(f"  Version: {requests.__version__}")
except ImportError:
    print("✗ requests module is NOT installed")
    print("  Install it with: pip install requests")

print()

# ============================================================================
# EXAMPLE 6: Using math module (built-in - no installation needed)
# ============================================================================

import math

print("=== Example 6: Using math module (built-in) ===")

numbers = [4, 9, 16, 25]
print("Number | Square Root | Power of 2")
print("-" * 35)

for num in numbers:
    sqrt_val = math.sqrt(num)
    pow_val = math.pow(num, 2)
    print(f"{num:6} | {sqrt_val:10.2f} | {pow_val:10.0f}")

print(f"\nPi value: {math.pi:.10f}")
print(f"E value: {math.e:.10f}")
print()


# ============================================================================
# EXAMPLE 7: Using random module (built-in)
# ============================================================================

import random

print("=== Example 7: Using random module (built-in) ===")

# Generate random numbers
print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random float (0-1): {random.random():.4f}")
print(f"Random float (1.5-4.5): {random.uniform(1.5, 4.5):.2f}")

# Random choice from list
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Random fruit: {random.choice(fruits)}")
print(f"Random sample (3 items): {random.sample(fruits, 3)}")

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")
print()


# ============================================================================
# QUICK REFERENCE: Common Pip Commands
# ============================================================================

print("=" * 60)
print("QUICK REFERENCE: Common Pip Commands")
print("=" * 60)
print("""
Install a package:
  pip install package_name

Install specific version:
  pip install package_name==version

Uninstall a package:
  pip uninstall package_name

List installed packages:
  pip list

Show package information:
  pip show package_name

Install from requirements.txt:
  pip install -r requirements.txt

Freeze packages to requirements.txt:
  pip freeze > requirements.txt

Upgrade a package:
  pip install --upgrade package_name

Search for a package:
  pip search package_name  (Note: search removed in pip 23.0+)
""")

