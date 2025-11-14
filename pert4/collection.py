# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# ============================================
# 1. LIST (ordered, changeable, duplicates allowed)
# ============================================
print("\n=== LIST EXAMPLE ===")
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")          # add to end
fruits.insert(1, "orange")      # insert at index
fruits.remove("banana")         # remove by value
popped_item = fruits.pop()      # remove last item
fruits.reverse()                # reverse order
fruits.sort()                   # sort list
count_apple = fruits.count("apple")  # count occurrences

print("Fruits:", fruits)
print("Popped item:", popped_item)
print("Count of 'apple':", count_apple)


# ============================================
# 2. TUPLE (ordered, not changeable, duplicates allowed)
# ============================================
print("\n=== TUPLE EXAMPLE ===")
numbers = (1, 2, 2, 3, 4)

print("Length:", len(numbers))       # count items
print("Index of 3:", numbers.index(3))
print("Count of 2:", numbers.count(2))

# Converting tuple to list
numbers_list = list(numbers)
print("Converted to list:", numbers_list)


# ============================================
# 3. SET (unordered, no duplicates)
# ============================================
print("\n=== SET EXAMPLE ===")
items = {"apple", "banana", "apple"}   # duplicates automatically removed

items.add("cherry")                    # add
items.update(["mango", "orange"])      # add multiple items
items.discard("banana")                # remove safely
# items.remove("banana")  # would cause error if not exist

random_item = items.pop()              # remove random item

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Items set:", items)
print("Random item removed:", random_item)
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))



