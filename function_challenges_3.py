# 7/10/2020, Blue/Brown, Nicolas Keck, 4 code challenges as assigned in class.

# Helper functions
def isPrime(num):
    a = num//2
    prime = True
    while a > 1:
        if float(num/a).is_integer() and float(num/a) != 1.0:
            prime = False
            break
        a -= 1
    return prime

# Blue function 1: Accepts a 6 digit ATM number and validates it against a variety
# of parameters.
def ATMvalid(pin):
    pin = str(pin)
    if len(pin) == 6 and int(pin[0])%2 == 0 and int(pin[5])%2 == 0 \
            and int(pin[2]) < int(pin[4]) and int(pin[1]) > int(pin[3]):
        sum = 0
        for num in pin:
            sum += int(num)
        return isPrime(sum)
    else:
        return False

pins = [291092, 310323]
for pin in pins:
    print(ATMvalid(pin))

# Brown function 1: Accepts a number and return an array filled with the numbers as many times...
def lengthener(number):
    out = []
    for num in str(number):
        if num != "0":
            out.append(num*int(num))
    return out

nums = [1230, 8032, 1234]
for num in nums:
    print(lengthener(num))

# Blue function 2: Accepts two same-size arrays and returns overlapping values
def overlaps(arr1, arr2):
    if len(arr1) == len(arr2):
        out = []
        for num1 in arr1:
            for num2 in arr2:
                if num1 == num2:
                    out.append(num1)
        return out
    else:
        return "Error"

# Normal case
array1 = [1, 2, 3, 4, 5, 6]
array2 = [2, 4, 6, 8, 10, 12]
print(overlaps(array1, array2))
# Wrong size case
array3 = []
print(overlaps(array1, array3))

# Brown function 2: Accepts a cc number and returns a masked version where only the
# last 4 digits are showing.
def ccCheck(cc):
    if len(cc.replace(" ", "")) == 16:
        return "**** "*3 + str(cc.split()[3])
    else:
        return "Invalid"

# Normal case
cc = "1234 5678 9101 1121"
print(ccCheck(cc))
# Invalid case
cc = "1"
print(ccCheck(cc))