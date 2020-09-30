# 9/30/2020, Nicolas Keck, Program which contains a bunch of example functions from class

# Returns the sum of two inputs
def findSum(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        return(n1+n2)
    else:
        raise TypeError("Inputs must be integers")
# n1 = 131927312
# n2 = 22
# print(findSum(n1, n2))


# Returns the factorial of an input
def factorial(num):
    total = 1
    for a in range(1, num+1):
        total *= a
    return total
# n1 = 10
# print(factorial(n1))


# Return the maximum and minimum value of three inputs(Could also be done with a sorted list)
def maxmin(n1, n2, n3):
    nums = [n1 , n2, n3]
    return min(nums), max(nums)
n1 = 10
n2 = 20
n3 = 100
print(maxmin(n1, n2, n3))


# Blue challenge 1: Creates an ATM function which accepts a four digit number and returns true if
# the sum of the pin is even
def ATM_Code(pin):
    if len(str(pin)) != 4:
        raise ValueError("Pin is too short")
    sum = 0
    for num in str(pin):
        sum += int(num)
    if sum%2 == 0:
        return True
    else:
        return False
# pins = [1111, 3234, 1134, 2310, 4902, 1230]
# for pin in pins:
#     print(ATM_Code(pin))


# Blue challenge 2: Creates a password function which return True if a password is strong, and false
# if it is weak.
import string
def passwordCheck(password):
    digit = False
    spechar = False
    if len(str(password)) > 8:
        for character in str(password):
            if character in string.digits:
                digit = True
            elif character in string.punctuation:
                spechar = True
            if digit and spechar:
                return True
        if not digit or not spechar:
            return False
    else:
        return False
    if digit and spechar:
        return True
# passwords = [123456789, "Joe", "Jimyty!23", "Password", ",./.,';/1/'", "Epic_gamer_123"]
# for password in passwords:
#     print(passwordCheck(password))