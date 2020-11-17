# 11/9/2020, Nicolas Keck, Converts a binary number into its denary equivalent

# Helper functions

# Find the length of a number without converting to a string
def intLen(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


# Modulo num seperator - example provided
"""
for a in range(len(num)):
    numSep(num, a) --> returns the n+1th digit of the number
"""
def numSep(num, a, l):
    return (num // 10**(l-a-1))%10

# Converts binary to denary
def binary_to_denary(num):
    denary = 0
    l = intLen(num)
    for a in range(l):
        denary += 2**(l-a-1) * numSep(num, a, l)
    return denary


# Converts denary to binary
def denary_to_binary(num):
    binary = ""
    while num != 1:
        binary += str(num%2)
        num = num//2
    binary += "1"
    binary = binary[::-1]
    return binary
number = 47806
#print(denary_to_binary(number))


# Converts binary to hex - Uses inputted string
letters = ["A", "B", "C", "D", "E", "F"]
def binary_to_hex(byte):
    hex = ""
    if len(byte)%4 != 0:
        byte = "0"*(4-len(byte)%4) + byte
    for a in range(int(len(byte)/4)):
        operand = ""
        for b in range(4):
            operand += byte[0]
            byte = byte.replace(byte[0], "", 1)
        n = binary_to_denary(int(operand))
        if n > 9:
            hex += letters[n%10]
        else:
            hex += str(n)
    return hex
byte = "1011101010111110"
#print(binary_to_hex(byte))

# Binary to hex(Better and for ints) - Fixed!
def binary_to_hex2(byte):
    hex = ""
    byte = binary_to_denary(byte)
    while byte != 0:
        if byte%16 > 9:
            hex += letters[byte%16-10]
        else:
            hex += str(byte%16)
        byte = byte//16
    return hex[::-1]
#print(binary_to_hex2(int(byte)))

# BABE = 47806
babe = 47806
print(denary_to_binary(babe))
print(babe)
print(binary_to_hex(denary_to_binary(babe)))