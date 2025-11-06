age = 20
sleep_hours = 10
coffee_cups = 0
assignments_due = False

if sleep_hours < 6 and coffee_cups == 0:
    print("Running on pure chaos and vibes 😵‍💫")
elif sleep_hours >= 6 and coffee_cups > 0:
    print("Fully charged Gen Z mode ☕💪 Let’s get this bread!")
elif assignments_due and (sleep_hours < 7 or coffee_cups < 1):
    print("Deadline anxiety unlocked 😭 better start now!")
elif assignments_due != True and sleep_hours >= 8:
    print("Rare moment of peace ✨ Netflix and scroll time 📱")
else:
    print("Just surviving, not thriving 😩")

