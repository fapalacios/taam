number = int(input("Enter integer: "))

while number != 0:
    if number%2 == 0:
        print(str(number) + " is an even number.")
    else:
        print(str(number) + " is an odd number.")
    number = int(input("Enter integer: "))

else:
    print("Bye!")