#9/9/2020, Nicolas Keck, Solutions to a variety of loop challenges

# Challenge 1: Accept any number and extract each digit using a for loop
num = int(input("Please input a number: "))
a = num
stack = []
for b in range(0, len(str(num))):
    stack.append(a%10)
    a = a//10
stack.reverse()
print(f"Digits: {str(stack).strip('[]')}")

# Challenge 2: Accept any number and print the sum of its digits
# (Will just use the number from before)
total = 0
for num in stack:
    total += num
print(f"Sum of digits: {total}")

# Challenge 3: Accept a number num, and print the first num values of the
# Fibonacci sequence
print("-------------------------------")
num = int(input("Please input another number: "))
output = [1, 1]
if num == 1:
    print(str(output).strip("[]"))
else:
    while len(output) != num:
        n = len(output)
        output.append(output[n-2] + output[n-1])
    print(str(output).strip("[]"))