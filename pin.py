PIN = "2752"

def verify_pin():
    attempts = 3

    while attempts > 0:
        user_pin = input("Enter your PIN: ")
        
        if user_pin == PIN:
            print("Access Granted, Welcome BOSS ")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN  Attempts left: {attempts}")

    print("Too many wrong attempts. Card blocked.")
    return False