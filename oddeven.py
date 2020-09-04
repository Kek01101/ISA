#4/9/2020, Blue, Nicolas Keck, Takes an input number and outputs the number of even and odd digits it has, as well as what digits those are
num = input("Please input a number: ")
odd = []
even = []
for digit in num:
    if int(digit)%2 == 0:
        even.append(digit)
    else:
        odd.append(digit)
print(f"{len(even)} even, {len(odd)} odd")
print(f"The even numbers were: {even}")
print(f"The odd numbers were: {odd}")