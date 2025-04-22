nums = [1, 5, 9, 11, 27, 55, 101]
find = 55

def binarySearch(nums, find, start, end):
    if start > end:
        print(find, "is not found in the list.")
        return

    mid = int((start + end) / 2)
    midVal = nums[mid]

    if midVal == find:
        print(find, "is found in the list.")
        return
    elif midVal < find:
        binarySearch(nums, find, mid + 1, end)
    else:
        binarySearch(nums, find, start, mid - 1)

binarySearch(nums, find, 0, len(nums) - 1)
