# Nicolas Keck, 19/10/2020, Functions from the practice array/functions IB paper
import string

# calcBMI function needed for the following questions
def calcBMI(H, W):
    x = H * H
    b = W / x
    return b

# This algorithm accepts a person's BMI and outputs the weight category they belong to
H = 2
W = 104
bmi = calcBMI(2, 104)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("overweight")
else:
    print("obese")

# Outputs the names of all people whose BMI is greater than a group's average BMI
name = ['a', 'b', 'c', 'd', 'e', 'f']
weight = [52, 100, 105, 61, 88, 68]
height = [1.56, 2, 2.03, 1.75, 1.8, 1.71]
average = 0
for a in range(len(name)):
    average += calcBMI(height[a], weight[a])
average = average/len(name)
for a in range(len(name)):
    if calcBMI(height[a], weight[a]) > average:
        print(name[a])

# Constructs an algorithim which creates an array where each letter in the alphabet has been
# shifted left n times
alphabet = string.ascii_uppercase
substitute = [None]*26
N = 5
for a in range(len(alphabet)):
    if a < N:
        substitute[a] = alphabet[a+(26-N)]
    else:
        substitute[a] = alphabet[a-N]
print(substitute)