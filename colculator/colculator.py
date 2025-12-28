# def replace_word():
#     str = "hi iam basem and hi hi hi hi"
#     word_to_replace = input("enter the word you want to replace : ")
#     word_replaced_with = input("enter the word you want to replace it with : ")
#     print(str.replace(word_to_replace, word_replaced_with))

# replace_word()

# number1 = int(input("enter the first number : "))
# number2 = int(input("enter the second number : "))
# user_choice = input("enter your choice (add, sub, mul, div) or (quit) to quit : ").lower()

def add_numbers(num1, num2):
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")

def sub_numbers(num1, num2):
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")

def mul_numbers(num1, num2):
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")

def div_numbers(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        answer = num1 / num2
        print(f"{num1} / {num2} = {answer}")

while True:
    try:
        num1 = int(input("enter the first number : "))
        num2 = int(input("enter the second number : "))
        user_choice = input("enter your choice (add, sub, mul, div) or (quit) to quit : ").lower()    
    except ValueError:
        print("invalid input")
        continue

    if user_choice == "add":
        add_numbers(num1, num2)
    elif user_choice == "sub":
        sub_numbers(num1, num2)
    elif user_choice == "mul":
        mul_numbers(num1, num2)
    elif user_choice == "div":
        div_numbers(num1, num2)
    elif user_choice == "quit":
        print("Goodbye!")
        break
    else:
        print("invalid choice")


