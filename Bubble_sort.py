# Nicolas Keck, 19/10/2020, Algorithim for buble sorting

# In algorithmic form:
nums = input("Enter numbers seperated by spaces: ").split(" ")
for a in range(len(nums)-1):
    for b in range(len(nums)-a-1):
        if int(nums[b]) > int(nums[b+1]):
            nums[b], nums[b+1] = nums[b+1], nums[b]
print(nums)

# In functional form:
def bubblesort(list):
    for a in range(len(list) - 1):
        for b in range(len(list) - a - 1):
            if int(list[b]) > int(list[b + 1]):
                list[b], list[b + 1] = list[b + 1], list[b]
    return list
