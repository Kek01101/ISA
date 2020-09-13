num = input("Please input a number: ")
if len(num) != 3:
    print("Invalid!")
else:
    output = ""
    for digit in num:
        for a in range(0, int(digit)):
            output += digit
    print(output)
