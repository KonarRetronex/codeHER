fruits = ["apple", "orange", "banana", "coconut", "durian", "anggur"]

print(fruits[:4:2])

my_list = []
n = int(input("How many items? "))

for i in range(n):
    item = input(f"Enter item {i+1}: ")
    my_list.append(item)

print(my_list)
