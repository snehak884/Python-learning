# String formatting

# name = "John"
# age = 25

# print("My name is %s and I am %d years old" % (name, age))
# # My name is John and I am 25 years old

# name = "John"
# age = 25

# print("My name is {} and I am {} years old".format(name, age))
# # My name is John and I am 25 years old

# # With position numbers
# print("My name is {0} and I am {1} years old".format(name, age))

# # With names
# print("My name is {n} and I am {a} years old".format(n=name, a=age))

# name = "John"
# age = 25
# salary = 50000.75

# print(f"My name is {name}")
# print(f"I am {age} years old")
# print(f"My salary is ${salary}")





template = "Dear {}, You are awesome. Take this {}$ bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s1 = template.format(a, a1)
print(s1)

print(f"{a} you are awesome and take this {a1}$ bag")