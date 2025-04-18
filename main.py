#By NN-Coder on Github at https://github.com/NN-Coder/binary-search/.
#Usable under MIT License; credit is due to me if the code is used.
#Note that the code could be more efficient with slicing or recursion.
#A simple input system could also be implemented to be more user-friendly.

#starting variables; change the numbers inside of nums and find
nums = [1, 5, 9, 11, 27, 55, 101]
#this should print '56 is not found in the list.'
find = 55
isFound = False

#function to find a usable midpoint (works for both even and odd amounts)
def findMid(length):
    return int((length - 1) / 2)

while not isFound and len(nums) > 0:
    #setting variables each recursion
    length = len(nums)
    mid = findMid(length)
    midVal = nums[mid]

    #main logic (halving list)
    if midVal == find:
        isFound = True

    else:
        temp = []
        for i in range(length):
            if midVal < find:
                if i > mid:
                    temp.append(nums[i])
            else:
                if i < mid:
                    temp.append(nums[i])

        nums = temp

#final return statements
if isFound:
    print(find, "is found in the list.")
    
else:
    print(find, "is not found in the list.")
