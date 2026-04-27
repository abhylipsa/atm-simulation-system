import balance
import statement

def withdraw_money():
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance.balance:
        print("Insufficient balance.")
    else:
        balance.balance -= amount
        record = f"Withdrawn: ₹{amount}"
        statement.add(record)
        print("Withdrawal successful.")  