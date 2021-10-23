while True:
    num = int(input("Enter a 10 digit number: "))

    length = len(str(num))
    if length == 10:
        last1 = int(str(num)[-1])
        last2 = int(str(num)[-2])

        sumL = last1 + last2

        if sumL < 10:
            print("Valid\n")
        else:
            print("Invalid\n")

    else:
        print("Enter a number with 10 digits.\n")
