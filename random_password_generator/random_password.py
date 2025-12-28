import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    try:
        password_length = int(input("Enter the length of the password (min 8): "))
        if password_length < 8:
            print("Password must be at least 8 characters!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    password = "".join(password)
    print(f"your password is: {password}")

generate_password()
