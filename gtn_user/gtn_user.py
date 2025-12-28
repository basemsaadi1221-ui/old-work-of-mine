import random


# def computer_guess(x):
#     number = int(input("enter your secret number: "))
#     computer_guess = 0
#     while computer_guess != number:
#         computer_guess = random.randint(1, x)
#         if computer_guess > number:
#             print(f"{computer_guess} is too high")
#         elif computer_guess < number:
#             print(f"{computer_guess} is too low")
#         else:
#             print(f"Your number is {computer_guess}")

# computer_guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #or high cuz h\l is equal
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C): ").lower()
        if feedback == "h":
            high = guess + 1
        elif feedback == "l":
            low = guess - 1
        elif feedback == "c":
            print(f"yay! the computer guessed your number {guess} correctly...")
        elif feedback != "h" or feedback != "l" or feedback != "c":
            print("please enter a valid feedback")

computer_guess(1000)