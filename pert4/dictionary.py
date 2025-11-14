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