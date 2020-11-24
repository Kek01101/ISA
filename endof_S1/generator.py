# This file serves to generate a sales array for the sales.csv file using random integers
from random import randint
import csv

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for a in range(10):
        line = [None]*12
        for b in range(12):
            line[b] = randint(100, 10000)
        writer.writerow(line)
