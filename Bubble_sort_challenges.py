# Nicolas Keck, 21/10/2020, In-class bubble sort challenges


# Sorting algorithim
def bSort(list):
    for a in range(len(list) - 1):
        for b in range(len(list) - a - 1):
            if list[b] > list[b + 1]:
                list[b], list[b + 1] = list[b + 1], list[b]
    return list

# Challenge 1 - Accepts numbers until -1 is entered, and then b-sorts the entries in either ascending or descending
# order
nums = []
while True:
    num = int(input("Please input numbers to sort: "))
    if num == -1:
        break
    else:
        nums.append(num)
nums = bSort(nums)
while True:
    answer = input("Ascending or descending?: ").upper()
    if answer == "ASCENDING":
        print(nums)
        break
    elif answer == "DESCENDING":
        nums.reverse()
        print(nums)
        break
    else:
        print("Not valid")

# Challenge 2 - Accepts either names or emails until quit is inputted and then sorts the inputted names in either
# ascending or descending order
while True:
    choice = input("Would you like to sort names or emails: ").upper()
    if choice  == "NAMES" or choice == "EMAILS":
        list = []
        break
    else:
        print('Not a valid choice')
while True:
    ins = input(f'Please input {choice.lower()}: ')
    if ins.upper() == 'QUIT':
        list = bSort(list)
        break
    else:
        list.append(ins)
while True:
    answer = input("Ascending or descending?: ").upper()
    if answer == "ASCENDING":
        print(list)
        break
    elif answer == "DESCENDING":
        list.reverse()
        print(list)
        break
    else:
        print("Not valid")
