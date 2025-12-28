import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"guess a number between 1 to {x}: "))
#         if guess > random_number:
#             print("try again... too high")
#         elif guess < random_number:
#             print("try again... too low")
#     else:
#         print(f"you guessed it right the number was {random_number}")

# guess(170)


def guess_game(x):
    computer_guess = random.randint(1, x)
    guess = 0
    lives = 7
    
    print(f"\nGuess a number between 1 and {x}. You have {lives} lives!")
    print("Type 'quit' to exit.\n")

    while lives > 0:
        user_input = input(f"Guess a number between 1 and {x}: ").lower()
        if user_input == "quit":
            print("You quit the game. Goodbye!")
            break   # Exit function
        try:
            user_guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if user_guess < 1 or user_guess > x:
            print(f"please enter a number between 1 to {x}")
            continue
        elif user_guess > computer_guess:
            print("try again... too high")
            lives -=1
            print(f"you have {lives} lives left")
        elif user_guess < computer_guess:
            print("try again... too low")
            lives -=1
            print(f"you have {lives} lives left")
        else:  # Correct guess
            print(f"\n🎉 Congratulations! You guessed it!")
            print(f"The number was {computer_guess}!")
            print("and you have {} lives left".format(lives))

    else:
        print(f"\n💀 Game Over! The number was {computer_guess}.")

guess_game(100)

