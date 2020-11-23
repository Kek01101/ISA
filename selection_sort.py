# Nicolas Keck, 21/10/2020, Implementation of selection sort

# In algorithmic form:
nums = input("Enter numbers seperated by spaces: ").split(" ")
for a in range(0, len(nums)-1):
    min = a
    for b in range(a+1, len(nums)):
        if int(nums[b]) < int(nums[min]):
            min = b
    nums[min], nums[a] = nums[a], nums[min]
print(nums)


# In functional form(Keep in mind that the integer function must be used for functional integer sort):
def selectionSort(nums):
    for a in range(0, len(nums) - 1):
        min = a
        for b in range(a + 1, len(nums)-1): # Many online sources use len(nums), but len(nums)-1 should work
            if int(nums[b]) < int(nums[min]):
                min = b
        if min != a:
            nums[min], nums[a] = nums[a], nums[min]
    return nums

# Selection sort for strings function:
def selectionSort(list):
    for a in range(0, len(list)):
        min = a
        for b in range(a+1, len(list)):
            if list[b] < list[min]:
                min = b
        if min != a: # Reduces time complexity
            list[min], list[a] = list[a], list[min]
    return list