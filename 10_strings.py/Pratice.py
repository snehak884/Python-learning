
name = "Alice Johnson"
age = 28
salary = 65000

print(f"Employee: {name}")
print(f"Age: {age} years old") 
print(f"Annual Salary: ${salary:,}")

print("Employee: {}".format(name))
print("Age: {} years old".format(age))
print("Annual Salary: ${:,}".format(salary))


name = input("Enter your name")
age = int(input("Enter your age"))
salary = float(input("Enter your salary"))

print(f"\n--- Personal Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Annual Salary: €{salary:,.2f}")
print(f"Monthly Salary: €{salary/12:.2f}")
