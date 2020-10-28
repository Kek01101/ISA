# Blue, Nicolas Keck, 28/10/2020, Creates a 2D array of size 4x4 that only accepts prime number


# Helper function
def isPrime(num):
    a = num//2
    prime = True
    while a > 1:
        if float(num/a).is_integer() and float(num/a) != 1.0:
            prime = False
            break
        a -= 1
    return prime


# Initialize arrays
grid = [[[None] for a in range(4)] for b in range(4)]
count = 3
for a in range(len(grid)):
    for b in range(len(grid[a])):
        while not isPrime(count):
            count += 1
        grid[a][b] = count
        count += 1


# Print array and diagonal
for a in range(len(grid)):
    print(grid[a])
print('Diagonal is:')
print(grid[0][0])
print(grid[1][1])
print(grid[2][2])
print(grid[3][3])