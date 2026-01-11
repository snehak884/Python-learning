# Create a list containing the table of 5


# table = []

# for i in range(1, 11):
#     table.append(5*i)

table = [5*i for i in range(1, 11)]

print(table)


# # Normal way
# squares = []
# for i in range(1, 6):
#     squares.append(i * i)
# print(squares)   # [1, 4, 9, 16, 25]

# List comprehension way

squares = [i * i for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
