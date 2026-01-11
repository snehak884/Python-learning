# Simple Salary Converter: Euro (€) to INR (₹)

# Taking inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
salary_euro = float(input("Enter your annual salary in Euro (€): "))

# Monthly salary in Euro
monthly_euro = salary_euro / 12

# Conversion rate (you can update as per current rate)
eur_to_inr = 102  

# Convert to INR
monthly_inr = monthly_euro * eur_to_inr

# Display result using f-string formatting
print("\n----- Salary Details -----")
print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"City      : {city}")
print(f"Annual Salary (EUR): €{salary_euro:,.2f}")
print(f"Monthly Salary (EUR): €{monthly_euro:,.2f}")
print(f"Monthly Salary (INR): ₹{monthly_inr:,.2f}")


# # Display result (no decimals)
# print("\n----- Salary Details -----")
# print(f"Name      : {name}")
# print(f"Age       : {age}")
# print(f"City      : {city}")
# print(f"Annual Salary (EUR): €{salary_euro:,}")
# print(f"Monthly Salary (EUR): €{monthly_euro:,}")
# print(f"Monthly Salary (INR): ₹{monthly_inr:,}")

