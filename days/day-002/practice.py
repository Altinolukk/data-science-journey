# Day 002 - Numbers, int vs float, strings, string methods

# Numbers
a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)      # float result
print("a // b =", a // b)    # integer division
print("a % b =", a % b)      # remainder
print("a ** b =", a ** b)    # power

# int vs float
x = 5
y = 5.0
print("type(x) =", type(x))
print("type(y) =", type(y))

# casting
print("float(x) =", float(x))
print("int(y) =", int(y))

# Strings
text = "hello world"
print("text =", text)
print("length =", len(text))
print("first char =", text[0])
print("slice =", text[0:5])

# String methods
print(text.upper())
print(text.capitalize())
print(text.replace("world", "python"))
print("contains 'wor'?", "wor" in text)

# Mini task
name = "Muhammet"
age = 21
print(f"My name is {name} and I am {age} years old.")
