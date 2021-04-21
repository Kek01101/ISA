import csv
from copy import deepcopy
import pandas as pd
import os

def load_data():
    masterlist = []
    with open(os.path.join(os.path.dirname(__file__), 'Recycling_Diversion_and_Capture_Rates.csv'), newline='') as file:
        reader = csv.reader(file)
        c = 0
        for row in reader:
            c += 1
            del (row[2])
            del (row[5])
            del (row[5])
            del (row[5])
            if c != 1:
                masterlist.append(row)
            else:
                toprow = row
    return masterlist, toprow


# Next goal: Sort by district, month, year
"""
Sort methods:
1) year
2) month
3) district
4) highest/lowest and reverse (hi/lo, lo/hi)


query = [None, None, None, None]
query[0] = None
query[1] = None
query[2] = 'Queens West'
query[3] = 'hi/lo'

"""


# New goal: Add None support - Added
# Other stuff: Multiple years? Best in a year? Best over many years? - Still need to decide
# Comparison --> One query vs another query - Yes
# Figure out how to select two or more types of cities, and how to make good selection in html - Done
def handle_query(query, masterlist):
    worklist = deepcopy(masterlist)
    for row in worklist:
        row[4] = float(row[4])
    for n in range(0,len(query)):
        if query[n] is not None:
            for row in deepcopy(worklist):
                if n == 0:
                    if row[2] not in query[n]:
                        worklist.remove(row)
                elif n == 1:
                    if row[3] not in query[n]:
                        worklist.remove(row)
                elif n == 2:
                    if row[0] not in query[n]:
                        worklist.remove(row)
            if n == 3:
                worklist = sorted(worklist, key=lambda x: x[4])
                if query[n] == 'hi/lo':
                    worklist.reverse()
    return worklist


def make_frame(worklist, name, toprow):
    with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), f"{name}.csv"), mode='w') as file:
        file.write(str(toprow).strip("[]").replace("'", "")+"\n")
        for line in worklist:
            file.write(str(line).strip("[]").replace("'", "")+"\n")
    with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), f"{name}.html"), mode='w') as file:
        file.write("<style>")
        file.write("    th {")
        file.write("        color: white;")
        file.write("    }")
        file.write("    td {")
        file.write("        color: white;")
        file.write("    }")
        file.write("</style>")
        file.writelines(pd.read_csv(os.path.join(os.path.realpath(os.path.dirname(__file__)), f"{name}.csv")).to_html())