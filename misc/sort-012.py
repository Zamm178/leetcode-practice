
def sortNums(nums):
    numsDict = {0: 0, 1: 0, 2: 0}
    res = []
    for n in nums:
        numsDict[n] += 1

    for key, value in numsDict.items():
        for i in range(value):
            res.append(key)
    return res


print(sortNums([1, 0, 2, 0, 1, 2, 2]))
