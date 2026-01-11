# Ask user for age
age = int(input("Enter your age: "))

# Assume user is a citizen (True/False can be set manually or asked via input)
citizen = True   # you can also ask user with input()

# Check voting eligibility
if age >= 18 and citizen:
    print("✅ Eligible to vote")
else:
    print("❌ Not eligible")


    
