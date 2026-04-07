# Day 003 - Lists, Dictionaries, Conditionals, Loops

# 1) Lists
scores = [70, 85, 90, 60, 100]
print("scores =", scores)
print("first score =", scores[0])
print("last score =", scores[-1])

scores.append(95)
print("after append =", scores)

# 2) Average calculation
average = sum(scores) / len(scores)
print("average =", average)

# 3) Dictionary
student = {
    "name": "Muhammet",
    "age": 21,
    "city": "Istanbul",
    "average": average,
}

print("student info =", student)
print("student name =", student["name"])

# 4) Conditionals
if average >= 85:
    status = "Excellent"
elif average >= 70:
    status = "Good"
elif average >= 50:
    status = "Pass"
else:
    status = "Fail"

print("status =", status)

# 5) Loop example
print("\nScore details:")
for i, score in enumerate(scores, start=1):
    print(f"{i}. score -> {score}")
