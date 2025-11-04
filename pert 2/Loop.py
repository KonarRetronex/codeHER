
for x in range (1, 11):
    print(f"Ini baris ke-{x}")


# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.
#
# --------------- EXAMPLE 1 ---------------

for x in range(1, 11):
   print(x)

# --------------- EXAMPLE 2 ---------------

for x in reversed(range(1, 11)):
   print(x)

print("Happy New Year!")

# --------------- EXAMPLE 3 ---------------

for x in range(1, 11, 2):
   print(x)

# --------------- EXAMPLE 4 ---------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)

# --------------- CONTINUE ---------------

for x in range(1, 21):
   if x == 13:
       continue
   else:
       print(x)

# --------------- BREAK ---------------

for x in range(1, 21):
   if x == 13:
       break
   else:
       print(x)


name = int(input("Enter your name: "))

while name == "":
    print("Name is empty, try again.")
    name = int(input("Enter your name: "))

print(f"Your name is {name}")
