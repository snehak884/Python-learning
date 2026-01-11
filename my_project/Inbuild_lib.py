import os

print("Current working directory:", os.getcwd())


print("Files in current directory:")
for file in os.listdir("."):   # "." = current directory
    print(file)


# Works like running commands in Mac terminal
os.system("echo Hello from Terminal!")

