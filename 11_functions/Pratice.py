def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")


# Function With Return Value

def add (a,b):
    return a + b

result = add(5,3)

print("sum is :", result)


# Function With Default Parameter

def greet(name ="Guest"):
    print("Welcome" , name)

greet()
greet("Alice")



    