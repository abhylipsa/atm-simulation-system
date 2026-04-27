import balance
import deposit
import withdraw
import statement
import pin

if not pin.verify_pin():
    exit()

while True:
    print("\n----- Welcome to Your ATM -----")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        balance.display_balance()

    elif choice == '2':
        deposit.deposit_money()

    elif choice == '3':
        withdraw.withdraw_money()

    elif choice == '4':
        statement.show_statement()

    elif choice == '5':
        print("Thanks for vibing with our ATM . See you again!")
        break

    else:
        print("Invalid choice.")