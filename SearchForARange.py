def searchRange(nums, target):
    return [findleft(nums,target), findright(nums,target)]

def findleft(nums, target):
    cand = -1
    return findleftHelper(nums, target, 0, -1)


def findleftHelper(nums, target, start, cand):
    
    #base case
    if (len(nums) == 0):
        return cand
    elif (len(nums) == 1 and nums[0] != target):
        return cand
    elif(len(nums) == 1 and nums[0] == target):
        return start

    
    else:
        i = int(len(nums) / 2)
        if (nums[i] > target):
            return findleftHelper(nums[:i], target, start, cand)
        elif (nums[i] < target):
            return findleftHelper(nums[i:],target, start + i, cand)
        elif(nums[i] == target and nums[i-1] != target):
            return start + i
        else:
            return findleftHelper(nums[:i], target, start, cand)


def findright(nums, target):
    cand = -1
    return findrightHelper(nums, target, 0, -1)

def findrightHelper(nums, target, start, cand):
    #base case
    if (len(nums) == 0):
        return cand
    elif (len(nums) == 1 and nums[0] != target):
        return cand
    elif(len(nums) == 1 and nums[0] == target):
        return start

    
    else:
        i = int(len(nums) / 2)
        if (nums[i] > target):
            return findrightHelper(nums[:i], target, start, cand)
        elif (nums[i] < target):
            return findrightHelper(nums[i:],target, start + i, cand)
        elif(nums[i] == target and (len(nums) > i + 1) and nums[i+1] != target):
            return start + i
        else:
            return findrightHelper(nums[i:], target, start+ i, cand)
    



#print(findleft([1,3,5,5,7,9,12],9))
#print(findright([1,3,5,5,7,9,12],9))


print(searchRange([1,3,5,5,7,9,12],9))
