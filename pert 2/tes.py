#
# operator = input("Enter your operator(/ + - *): ")
# num1 = float(input("Enter your first number: "))
# num2 = float(input("Enter your second number: "))
#
# if operator == "/":
#     result = num1 / num2
# elif operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# else:
#     print("Invalid operator!")
# if result.is_integer(): result = int(result)
# if num1.is_integer(): num1 = int(num1)
# if num2.is_integer(): num2 = int(num2)
#
# print(f"{num1}{operator}{num2}:", result)


#
#
# day = "saturday"
# age = 18
#
# match day:
#     case "monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print("Kuliah woyy")
#     case n if day == "saturday" or "sunday" and age >= 18:
#         print("Libur")
#     case _:
#         print("Invalid day!")
#
# match day:
#     case "monday":
#         print("Kuliah woyy")
#     case "Tuesday":
#         print("Kuliah woyy")
#     case "Wednesday":
#         print("Kuliah woyy")
#     case "Thursday":
#         print("Kuliah woyy")
#     case "Friday":
#         print("Kuliah woyy")
#     case "Saturday":
#         print("Lbur yey")
#     case "Sunday":
#         print("Libur yey")
#
#
#
# if day == "monday" or age == "tuesday":
#     print("Kuliah woyy")
#
#
# age = 20
# sleep_hours = 10
# coffee_cups = 0
# assignments_due = False
#
# if sleep_hours < 6 and coffee_cups == 0:
#     print("Running on pure chaos and vibes 😵‍💫")
# elif sleep_hours >= 6 and coffee_cups > 0:
#     print("Fully charged Gen Z mode ☕💪 Let’s get this bread!")
# elif assignments_due and (sleep_hours < 7 or coffee_cups < 1):
#     print("Deadline anxiety unlocked 😭 better start now!")
# elif assignments_due != True and sleep_hours >= 8:
#     print("Rare moment of peace ✨ Netflix and scroll time 📱")
# else:
#     print("Just surviving, not thriving 😩")
#

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




