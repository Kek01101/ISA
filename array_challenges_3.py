# 18/9/2020, Blue, Nicolas Keck, Accepts an array of student names and scores and
# prints the student with the highest score.

# Blue challenge: Explained above
names = input("Please input student names(Seperated by commas): ").split(", ")
scores = input("Please input corresponding scores(Seperated by commas): ").split(", ")
tuples = []
for a in range(0, len(names)):
    tuples.append((int(scores[a]), names[a]))
tuples.sort()
tuples.reverse()
print(tuples[0][1], tuples[0][0])

# Brown challenge: Accepts an array and outputs a second array with the factorials for the nums in the first one
nums = input("Please input some numbers: ").split(", ")
output = []
for a in range(0, len(nums)):
    num = int(nums[a])
    count = num
    while count > 1:
        print(num)
        count -= 1
        num *= count
    output.append(num)
print(output)