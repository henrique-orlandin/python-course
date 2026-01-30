x = 10
boolean = True
print(x)
print(type(x))

y = "hello,"
y += " world"
print(y)

# logic operators (and/or/not)

# checks if the variable uses same memory slot
print(x is not y)

names = ["Ana", "John", "John"]
print("Ana" in names)
print("John" not in names)

if x >= 10:
    print("x is greater than 10")
else:
    print("x is less than 10")