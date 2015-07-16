def summaryRanges(nums):
    result = []
    ele = 1
    i = 0
    starti = 0
    while (i < len(nums)):
        if (i == (len(nums) - 1)):
            if (ele == 1) and (len(nums) == 1):
                result.append(str(nums[i]))
            elif ((nums[i - 1] + 1) != nums[i]):
                result.append(str(nums[i]))            
            else:
                result.append(str(nums[starti]) + "->" + str(nums[i]))
        else:
            if((nums[i] + 1) != nums[i + 1]):
                if(ele == 1):
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[starti]) + "->" + str(nums[i]))
                starti = i + 1
                ele = 1
            else:
                ele += 1
        i += 1
    return result

print(summaryRanges([-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000]))

