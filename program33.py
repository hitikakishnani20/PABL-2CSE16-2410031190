# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.
def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i+1, target-candidates[i], path+[candidates[i]])

    backtrack(0, target, [])
    return res