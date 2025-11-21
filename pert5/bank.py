
def show_balance():
    print(f"Your balance is: Rp{balance:,}")

def deposit():
    try:
        deposit_amount = int(input("Enter the amount you want to deposit: "))


        if deposit_amount < 0:
            print("amount cannot be negative")
            return 0
        else:
            return deposit_amount

    except ValueError:
        print("please enter a valid number")
        return 0


def withdraw():
    try:

        withdraw_amount = int(input("Enter the amount you want to withdraw: "))

        if withdraw_amount > balance:
            print("You cannot withdraw more than your current balance")
            return 0
        elif withdraw_amount < 0:
            print("Dont use the '-' sign, just type the amount you want: ")
            return 0
        else:
            return withdraw_amount
    except ValueError:
        print("Please enter a valid number")
        return 0


balance = 0
is_running = True

while is_running == True:
    print("*********************************")
    print("         Banking Program         ")
    print("*********************************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit Program")
    print("*********************************")
    choice = input("Enter a Choice (1-4): ")


    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
        print(f"Your current balance is: {balance:,}")
    elif choice == "3":
        balance -= withdraw()
        print(f"Your current balance is: {balance:,}")
    elif choice == "4":
        is_running = False
    else:
        print("That's not a valid choice")

print("*********************************")
print("     Thank You, see you later    ")
print("*********************************")
