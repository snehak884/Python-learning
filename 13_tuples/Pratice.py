
# Create 

fruits = ("apple", "banana", "cherry")

print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[0:2])   # ('apple', 'banana') (slicing)


person = ("Alice", 25, "London")
print(person)          # ('Alice', 25, 'London')
print(f"Name: {person[0]}, Age: {person[1]}, City: {person[2]}")


nested = (1, (2, 3), (4, 5))
print(nested[1])       # (2, 3)
print(nested[1][0])    # 2



name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Unpacked 

person = ("Bob", 30, "New York")

# Unpacking
name, age, city = person

print(name)   # Bob
print(age)    # 30
print(city)   # New York
