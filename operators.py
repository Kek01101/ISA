#2/9/2020, Blue, Nicolas Keck, Takes an input number and outputs its individual numbers
num = int(input("Please input your number: "))
stack = []
while num > 0:
    stack.append(num%10)
    num = num//10
while stack:
    print(stack.pop())