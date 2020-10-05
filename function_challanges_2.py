# Brown/Blue, Nicolas Keck, 10/5/2020, Function challenges from in-class wrok

# Accepts an array and totals the values within(Does not total negative numbers)
def arrayTotal(array):
    total = 0
    for num in array:
        if num > 0:
            total += num
    return total

l1 = [10, -100, 5]
# print(arrayTotal(l1))


# Accepts three arrays, Student name, grade, and advisor name. Then takes another arg for a student
# name. Then returns that student's grade level and advisor name. Uses b-search and returns not
# found if not found. This is the blue challenge. (Case sensisitve)
def sorter(list):
    return list[0]
def school(students, grades, advisors, name_in):
    sortlist = []
    for a in range(len(students)):
        sortlist.append((students[a], grades[a], advisors[a]))
    sortlist.sort(key=sorter)
    a = 0
    high = len(students)-1
    low = 0
    operations = 0
    while name_in != sortlist[a][0]:
        a = ((high + low) // 2)
        if name_in == sortlist[a][0] or operations > len(students):
            break
        elif name_in < sortlist[a][0]:
            high = a - 1
        else:
            low = a + 1
        operations += 1
    if operations > len(students):
        return "Not Found"
    else:
        return sortlist[a][1], sortlist[a][2]


students = ["Guy", "Chad", "Stacy", "Nam", "Name", "Other name", "That guy"]
grades = [11, 10, 2, 1, 6, 7, 8]
advisors = ["Mr. A", "Mr. B", "Mr. C", "Mr. Ez", "Mr. Clean", "Ms. Other", "Mrs. Married", "Mr. Eight"]
print(school(students, grades, advisors, "Guy"))


# Accepts an array of names, and outputs an array containing the number of vowels in each name.
# This is the brown challenge.
def vowelCount(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count

def vowelizer(names):
    counts = []
    for name in names:
        counts.append(vowelCount(name))
    return counts

names = ["Wow", "Woow", "Other thing", "LOTSA VOWELS", "n"]
print(vowelizer(names))