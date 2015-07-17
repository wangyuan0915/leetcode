def productExceptSelf(nums):
    left = 1
    right = 1
    leftlist = []
    rightlist = []
    result = []
    for i in range(len(nums)):
        leftlist.append(left*nums[i])
        left *= nums[i]
        rightlist.append(right*nums[len(nums) - 1- i])
        right *= nums[len(nums) - 1- i]

    print(leftlist)
    print(rightlist)

    for i in range(len(nums)):
        if (i == 0):
            result.append(rightlist[len(nums) - 2])
        elif(i == (len(nums) - 1)):
            result.append(leftlist[len(nums) - 2])
        else:
            result.append(leftlist[i - 1]*rightlist[(len(nums) - i - 2)])

    print(result)
    return result


productExceptSelf([1,2,3,4])
