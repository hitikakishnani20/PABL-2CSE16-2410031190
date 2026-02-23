# Given an integer array nums of unique elements, return all possible subsets (the power set).
def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path)
        for i in range(start, len(nums)):
            backtrack(i+1, path+[nums[i]])

    backtrack(0, [])
    return res