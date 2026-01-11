
# score = 87

# if score > 90:
#       print ("you got A grade")
# elif score > 80:
#       print ("you got B garde")
# else : 
#       print("Congrats , you are pass")



# weather condition 

temperature = 25

if temperature > 30:
    print("It's very hot!")
elif temperature > 20:
    print("Nice weather")
elif temperature > 10:
    print("A bit cool")
elif temperature > 0:
    print("Cold weather")
else:
    print("Freezing!")


#Age categories 

age = 25

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"You are a {category}")



# example with input statement 

score = int(input("Enter your score (0-100)"))

if score >= 90:
    print("Excellent! Grade: A")
elif score >= 80:
    print("Good job! Grade: B")
elif score >= 70:
    print("Well done! Grade: C")
elif score >= 60:
    print("You passed! Grade: D")
else:
    print("Sorry, you failed. Grade: F")




print("=== Restaurant Menu ===")
print("1. Pizza - $12")
print("2. Burger - $8")
print("3. Salad - $6")
print("4. Pasta - $10")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("You ordered Pizza - $12")
elif choice == 2:
    print("You ordered Burger - $8")
elif choice == 3:
    print("You ordered Salad - $6")
elif choice == 4:
    print("You ordered Pasta - $10")
else:
    print("Invalid choice! Please select 1-4")


'''

Key Points to Remember:

Order matters: Python checks conditions from top to bottom and stops at the first true condition
Only one block executes: Even if multiple conditions are true, only the first true condition's block runs
elif is short for "else if": You can have multiple elif statements
else is optional: You don't always need an else clause
Indentation is crucial: Python uses indentation to define code blocks

'''