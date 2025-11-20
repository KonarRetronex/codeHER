import random

print("\n=== random.random() ===")
print(random.random())   # float 0–1


print("\n=== random.randint(1, 10) ===")
print(random.randint(1, 10))  # integer 1–10


print("\n=== random.randrange(5, 20) ===")
print(random.randrange(5, 20))  # 5–19


print("\n=== random.choice() ===")
fruits = ["apple", "banana", "cherry", "mango"]
print("Random fruit:", random.choice(fruits))


print("\n=== random.choices() (with duplicates) ===")
print(random.choices(fruits, k=3))


print("\n=== random.sample() (unique items) ===")
print(random.sample(fruits, 2))


print("\n=== random.shuffle() ===")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)


print("\n=== random.uniform(1, 5) ===")
print(random.uniform(1, 5))   # float between 1–5
