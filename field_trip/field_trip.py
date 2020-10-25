# Blue, Nicolas Keck, 26/10/2020, Generates unique codes for people in a class based upon
# their birth date. Find accompanying student data in the field_trip.csv file.
# Extension: Using a csv file to input data instead of manual input
import csv


def codify(month, year):
    code = month + year
    total = 0
    for num in str(code):
        total += int(num)
    return total


def sSort(nums, names):
    for a in range(0, len(nums)-1):
        min = a
        for b in range(a+1, len(nums)-1):
            if nums[b] < nums[min]:
                min = b
        if min != a:
            nums[min], nums[a] = nums[a], nums[min]
            names[min], names[a] = names[a], names[min]


def main():
    names = []
    birthdays = []
    codes = [None]*21
    with open('field_trip.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row[0])
            birthdays.append((row[1], row[2]))
    for a in range(len(names)):
        codes[a] = codify(int(birthdays[a][0]), int(birthdays[a][1]))
    sSort(codes, names)
    print('Sorted list below: ')
    for a in range(len(names)):
        print(f'{names[a]}, {codes[a]}')


if __name__ == '__main__':
    main()