# 25/11/2020, Nicolas Keck, HL End of semester assignment source code


"""
Initialization:
Here the sales array is imported from the 'sales.csv' file, libraries are imported,
and some useful lists are created.
"""
# Importing
import csv

# Lists
sales = [[None for a in range(12)] for b in range(10)]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# CSV reader
with open('sales.csv', newline='') as file:
    reader = csv.reader(file)
    a = 0
    for row in reader:
        b = 0
        for column in row:
            sales[a][b] = column
            b += 1
        a += 1


"""
Question a: Write a function that prints out the months that had the most and least sales
"""
maxsales = 0
maxmonth = 0
minsales = float('inf')
minmonth = 0
for columns in range(12):
    total = 0
    for rows in range(10):
        total += int(sales[rows][columns])
    if total > maxsales:
        maxsales = total
        maxmonth = months[columns]
    elif total < minsales:
        minsales = total
        minmonth = months[columns]
print("Question a:")
print(f"Month with most sales: {maxmonth}")
print(f"Month with least sales: {minmonth}")
print("\n")

"""
Question b: Write a function that accepts a zone number (1-10 only) and returns the total sales for the year for that
particular zone.
"""
print("Question b:")
zone = int(input("Please input a zone: ")) - 1
if zone < 0 or zone > 9:
    raise Exception("Zone out of bounds")
else:
    total = 0
    for columns in range(12):
        total += int(sales[zone][columns])
    print(f"Total sales from zone {zone+1}: {total}")
    print("\n")


"""
Question c: Write a function that prints out all the zones that had better sales in the second half of the year (July -
Dec) than the first one (Jan – Jun). Add the qualifying zone numbers into a queue and display.
"""
queue = []
for rows in range(10):
    firsthalf = 0
    secondhalf = 0
    for columns in range(12):
        if columns > 5:
            secondhalf += int(sales[rows][columns])
        else:
            firsthalf += int(sales[rows][columns])
    if secondhalf > firsthalf:
        queue.append(rows+1)
print("Question c:\nZones with better second halves-")
while queue:
    print(f"Zone {queue.pop(0)}")
print("\n")


"""
Question d: Write a function that checks which zones sold lesser units than that month’s all zone average. Add the
qualifying zones into a stack and display along with month name.
"""
stack = []
for columns in range(12):
    average = 0
    below = str(months[columns]) + " 2019:"
    for rows in range(10):
        average += int(sales[rows][columns])
    average = average // 12
    for rows in range(10):
        if int(sales[rows][columns]) < average:
            below = below + " " + str(rows+1)
    stack.append(below)
print("Question d:\nZones which performed below the average-")
while stack:
    print(stack.pop())
print("\n")


"""
Question e: Write a function that prints out a final end of the year sales report (Jan - Dec) sorted by most sales in a
zone to the least.
"""
monthreport = [[None for a in range(10)] for b in range(12)]
for columns in range(12):
    performances = [None]*10
    zones = [None]*10
    for rows in range(10):
        performances[rows] = int(sales[rows][columns])
        zones[rows] = rows
    for a in range(len(performances)):
        max = a
        for b in range(a+1, len(performances)):
            if int(performances[b]) > int(performances[max]):
                max = b
        if max != a:
            performances[max], performances[a] = performances[a], performances[max]
            zones[max], zones[a] = zones[a], zones[max]
    for rows in range(10):
        monthreport[columns][rows] = "Zone " + str(zones[rows]+1) + ": " + str(performances[rows])
print("Question e:\nEnd of year sales report--")
for month in range(12):
    print(f"{months[month]} report-")
    for zones in range(10):
        print(monthreport[month][zones])
    print("")
