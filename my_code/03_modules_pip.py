"""
PYTHON MODULES, LIBRARIES, AND PIP - COMPLETE GUIDE
===================================================

This tutorial explains:
1. What are Modules?
2. What are Libraries?
3. Are Modules and Libraries the same?
4. What is Pip?
5. How to use Built-in Modules
6. How to use External Modules
"""

# ============================================================================
# PART 1: WHAT IS A MODULE?
# ============================================================================

"""
A MODULE is a file containing Python code (functions, classes, variables, etc.)
that can be imported and used in other Python programs.

Think of a module as a toolbox - it contains tools (functions/classes) that
you can use in your code without having to write them yourself.
"""

# ============================================================================
# PART 2: TYPES OF MODULES
# ============================================================================

# 1. BUILT-IN MODULES (come with Python - no installation needed)
# Examples: math, os, sys, random, datetime, json, etc.

# 2. EXTERNAL/THIRD-PARTY MODULES (need to be installed)
# Examples: requests, numpy, pandas, flask, django, etc.

# 3. CUSTOM MODULES (modules you create yourself)
# Examples: mymodule.py, utils.py, helpers.py, etc.


# ============================================================================
# PART 3: WHAT IS A LIBRARY?
# ============================================================================

"""
A LIBRARY is a collection of modules. It's a broader term.

- A module is a single file
- A library is a collection of related modules packaged together
- A package is a directory containing multiple modules

In practice, people often use "module" and "library" interchangeably,
but technically:
- math is a MODULE (single file)
- requests is a LIBRARY (contains multiple modules)
- numpy is a LIBRARY (contains many modules)
"""

# ============================================================================
# PART 4: MODULES vs LIBRARIES - ARE THEY THE SAME?
# ============================================================================

"""
Technically NO, but in practice people use them interchangeably:

MODULE:
- A single .py file containing Python code
- Example: math.py, random.py

LIBRARY/PACKAGE:
- A collection of related modules
- Usually a folder with multiple .py files
- Example: requests (has multiple modules inside), numpy (has many modules)

COMMON USAGE:
- People often say "import a library" when they mean "import a module"
- Both terms are acceptable in everyday conversation
- The Python documentation uses "module" more precisely
"""

# ============================================================================
# PART 5: USING BUILT-IN MODULES (No installation needed)
# ============================================================================

# Example 1: Math module
import math

print("=== MATH MODULE ===")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")
print(f"2 to the power of 3: {math.pow(2, 3)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print()


# Example 2: Random module
import random

print("=== RANDOM MODULE ===")
print(f"Random number 0-10: {random.randint(0, 10)}")
print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")
print(f"Random float 0-1: {random.random()}")
print()


# Example 3: DateTime module
from datetime import datetime, date, timedelta

print("=== DATETIME MODULE ===")
now = datetime.now()
print(f"Current date and time: {now}")
print(f"Today's date: {date.today()}")
print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print()


# Example 4: OS module
import os

print("=== OS MODULE ===")
print(f"Current working directory: {os.getcwd()}")
print(f"Operating system: {os.name}")
print(f"Path separator: {os.sep}")
print()


# Example 5: Different import methods
import sys
from math import sqrt, pi  # Import specific functions
from random import randint as randi  # Import with alias

print("=== DIFFERENT IMPORT METHODS ===")
print(f"Using math.sqrt directly: {sqrt(16)}")
print(f"Using pi directly: {pi}")
print(f"Random with alias: {randi(1, 100)}")
print()


# ============================================================================
# PART 6: WHAT IS PIP?
# ============================================================================

"""
PIP stands for "Pip Installs Packages" (or "Pip Installs Python")

PIP is:
- The package installer for Python
- A command-line tool that comes with Python
- Used to install external/third-party modules/libraries
- Connects to PyPI (Python Package Index) - a repository of Python packages

Think of pip as an app store for Python - you use it to download and install
external libraries that don't come with Python by default.
"""

# ============================================================================
# PART 7: HOW TO USE PIP - COMMON COMMANDS
# ============================================================================

"""
BASIC PIP COMMANDS (run these in terminal/command prompt):

1. Check if pip is installed:
   pip --version
   OR
   pip3 --version

2. Install a package:
   pip install package_name
   Example: pip install requests

3. Install a specific version:
   pip install package_name==version
   Example: pip install requests==2.28.0

4. Uninstall a package:
   pip uninstall package_name

5. List installed packages:
   pip list

6. Show package info:
   pip show package_name

7. Install from requirements.txt:
   pip install -r requirements.txt

8. Save installed packages to requirements.txt:
   pip freeze > requirements.txt

9. Upgrade a package:
   pip install --upgrade package_name
"""

# ============================================================================
# PART 8: HOW TO USE EXTERNAL MODULES (Step by Step)
# ============================================================================

"""
STEP-BY-STEP GUIDE TO USING EXTERNAL MODULES:

Step 1: Install the module using pip
   pip install module_name

Step 2: Import the module in your Python file
   import module_name

Step 3: Use the module's functions/classes
   module_name.function_name()
"""

# ============================================================================
# PART 9: EXAMPLE - Using 'requests' External Module
# ============================================================================

"""
First, you would install it in terminal:
   pip install requests

Then use it in your code:
"""

# Uncomment the code below after installing requests:
# import requests
#
# print("=== REQUESTS MODULE (External) ===")
# 
# # Make a GET request to a website
# response = requests.get('https://api.github.com')
# print(f"Status code: {response.status_code}")
# print(f"Response headers: {dict(list(response.headers.items())[:3])}")
# print()


# ============================================================================
# PART 10: EXAMPLE - Using 'colorama' External Module (if installed)
# ============================================================================

"""
Install: pip install colorama
Use: Add colors to terminal output
"""

# Uncomment after installing colorama:
# from colorama import Fore, Back, Style, init
# init()  # Initialize colorama
# 
# print("=== COLORAMA MODULE (External) ===")
# print(f"{Fore.RED}This text is red!")
# print(f"{Fore.GREEN}This text is green!")
# print(f"{Fore.BLUE}This text is blue!")
# print(f"{Style.RESET_ALL}Back to normal color")
# print()


# ============================================================================
# PART 11: CREATING YOUR OWN MODULE
# ============================================================================

"""
You can create your own module! Just create a .py file and import it.

Example: Create a file called 'my_utils.py' with:
"""

# my_utils.py content (example):
"""
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
"""

# Then in another file, you can import it:
# import my_utils
# print(my_utils.greet("Alice"))
# print(my_utils.add(5, 3))
# print(my_utils.PI)


# ============================================================================
# PART 12: REQUIREMENTS.TXT FILE
# ============================================================================

"""
When working on a project, you should create a requirements.txt file
that lists all external modules your project needs.

Example requirements.txt:
-------------------
requests==2.28.0
numpy==1.23.0
pandas==1.5.0
flask==2.2.0
-------------------

Then others can install all dependencies with:
   pip install -r requirements.txt
"""

# ============================================================================
# PART 13: VIRTUAL ENVIRONMENTS (Best Practice)
# ============================================================================

"""
VIRTUAL ENVIRONMENTS are isolated Python environments for your projects.

Why use them?
- Keep dependencies separate for different projects
- Avoid version conflicts
- Keep your system Python clean

How to create one:
   python -m venv venv_name

How to activate:
   Windows: venv_name\Scripts\activate
   Mac/Linux: source venv_name/bin/activate

How to deactivate:
   deactivate
"""

# ============================================================================
# PART 14: COMMON EXTERNAL MODULES & THEIR USES
# ============================================================================

"""
requests      - Make HTTP requests (API calls)
numpy         - Numerical computing (arrays, math)
pandas        - Data manipulation and analysis
flask         - Web framework (create web apps)
django        - Full-featured web framework
beautifulsoup4 - Web scraping (parse HTML/XML)
pillow        - Image processing
matplotlib    - Data visualization (charts/graphs)
scikit-learn  - Machine learning
selenium      - Web automation/browser testing
"""

# ============================================================================
# PART 15: SUMMARY
# ============================================================================

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
MODULE:
  - A single .py file with reusable code
  - Can be built-in, external, or custom

LIBRARY:
  - Collection of related modules
  - In practice, often used interchangeably with "module"

PIP:
  - Package installer for Python
  - Used to install external modules/libraries
  - Command: pip install package_name

USING EXTERNAL MODULES:
  1. Install: pip install module_name
  2. Import: import module_name
  3. Use: module_name.function()

BUILT-IN MODULES:
  - Come with Python (no installation needed)
  - Examples: math, random, datetime, os, sys

EXTERNAL MODULES:
  - Need to be installed with pip
  - Examples: requests, numpy, pandas
""")

