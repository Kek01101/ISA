# 21/9/2020, Blue, Nicolas Keck, Imports a number of timestamps and tweets and uses binary search
# to find a tweet given a timestamp. Small problem being that some tweets have the same timestamp.
import csv
def tupsort(list):
    return(list[0])
data = []
with open("tweets.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append((row[0], row[1]))
data.sort(key=tupsort)
stamp = input("Please input a timestamp: ")
real = 0
high = len(data)-1
low = 0
while stamp != data[real][0]:
    real = ((high + low) // 2)
    if stamp == data[real][0]:
        break
    elif stamp < data[real][0]:
        high = real - 1
    else:
        low = real + 1
print(data[real][1])
