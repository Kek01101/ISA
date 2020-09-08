#7/9/2020, Blue, Nicolas Keck, Takes a number an prints out all the primes between 3 and that number
a = input("Please input a number: ")
for a in range(3,int(a)+1):
    prime = True
    b = a
    while b > 1:
        if float(a/b).is_integer() and float(a/b) != 1.0:
            prime = False
            break
        b -= 1
    if prime:
        print(a)
