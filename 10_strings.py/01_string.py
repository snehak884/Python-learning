# # name = "Harry"
# name = 'Sneha'
# # name = '''Harry is a good boy'''
# print(name)


# company = '''I joined yoummday in the month of June
# Overall it is very good experience 
# I Learned couple think which i will be utilized in my next career path'''

# print(company)


# Different ways to create strings
name = "John"           # Double quotes
city = 'New York'       # Single quotes
message = """Hello
World"""                # Triple quotes (multi-line)

print(name)    # John
print(city)    # New York
print(message) # Hello
               # World



text = "Python"
#       012345  (positive indexing)
#      -654321  (negative indexing)

print(text[0])    # P (first character)
print(text[1])    # y
print(text[5])    # n (last character)

# # Negative indexing (from the end)

print(text[-1])   # n (last character)
print(text[-2])   # o (second last)
print(text[-6])   # P (first character)


text = "Programming"
#       01234567890

print(text[0:4])      # Prog (from 0 to 3)
print(text[4:8])      # ramm (from 4 to 7)
print(text[8:])       # ing (from 8 to end)
print(text[:4])       # Prog (from start to 3)
print(text[:])        # Programming (entire string)


