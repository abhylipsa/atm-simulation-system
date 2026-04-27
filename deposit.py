import balance
import statement

def deposit_money():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance.balance += amount   
        record = f"Deposited: ₹{amount}"
        statement.add(record)
        print("Deposit successful.")
    else:
        print("Invalid amount.")



