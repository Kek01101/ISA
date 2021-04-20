import csv
from copy import deepcopy
import pandas as pd

masterlist = []
with open('Recycling_Diversion_and_Capture_Rates.csv', newline='') as file:
    reader = csv.reader(file)
    c = 0
    for row in reader:
        c += 1
        del (row[2])
        del (row[5])
        del (row[5])
        del (row[5])
        if c == 1000:
            break
        elif c != 1:
            masterlist.append(row)
        else:
            toprow = row

# Next goal: Sort by district, month, year
"""
Sort methods:
1) year
2) month
3) district
4) highest/lowest and reverse (hi/lo, lo/hi)
"""

query = [None, None, None, None]
query[0] = None
query[1] = None
query[2] = 'Queens West'
query[3] = 'hi/lo'

worklist = deepcopy(masterlist)

# New goal: Add None support - Added
# Other stuff: Multiple years? Best in a year? Best over many years?
# Comparison --> One query vs another query
# Figure out how to select two or more types of cities, and how to make good selection in html
for row in worklist:
    row[2] = int(row[2])
    row[4] = float(row[4])
for n in range(0,len(query)):
    if query[n] is not None:
        for row in deepcopy(worklist):
            if n == 0:
                if query[n] != row[2]:
                    worklist.remove(row)
            elif n == 1:
                if query[n] != row[3]:
                    worklist.remove(row)
            elif n == 2:
                if query[n] != row[0]:
                    worklist.remove(row)
        if n == 3:
            worklist = sorted(worklist, key=lambda x: x[4])
            if query[n] == 'hi/lo':
                worklist.reverse()
with open("output.csv", mode='w') as file:
    file.write(str(toprow).strip("[]").replace("'", "")+"\n")
    for line in worklist:
        file.write(str(line).strip("[]").replace("'", "")+"\n")
with open("output.html", mode='w') as file:
    file.writelines(pd.read_csv("output.csv").to_html())
