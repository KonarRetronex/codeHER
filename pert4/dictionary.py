# ============================================
# 4. DICTIONARY (key-value pairs)
# ============================================
print("\n=== DICTIONARY EXAMPLE ===")
student = {
    "name": "John",
    "age": 20,
}

student["age"] = 21                # update value
student["class"] = "A"             # add new key-value
age_value = student.get("age")     # safe get
removed_item = student.pop("class")    # remove specific key
last_pair = student.popitem()      # remove last inserted

print("Student dict:", student)
print("Age:", age_value)
print("Removed item:", removed_item)
print("Last popped pair:", last_pair)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student = {"name": "John", "age": 20, "class": "A"}

for key in student:
    print(key)

for key in student.keys():
    print(key)

student = {"name": "John", "age": 20, "class": "A"}

for value in student.values():
    print(value)


# Dictionary example
student = {
    "name": "John",
    "age": 20,
    "class": "A",
    "score": 88
}

# Loop through key and value
for key, value in student.items():
    print(key, ":", value)
