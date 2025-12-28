def dollar_to_dinnar(rate = 1500):
    try:
        dollar = float(input("Enter the amount of dollar you want to convert: "))
        if dollar < 0:
            print("Amount cannot be negative!")
            return
    except ValueError:
        print("Please enter a valid number")
        return
    dinar = dollar * rate
    print(f"your amount in dinnar for ${dollar:.2f} is: {dinar:.2f} IQD")


dollar_to_dinnar(rate=1490)