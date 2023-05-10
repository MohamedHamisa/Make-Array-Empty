class Solution:
    def countOperationsToEmptyArray(self, nums):
        n, res, turn = len(nums), 1, 1
        idx = sorted(range(n), key=lambda x: nums[x])
        for i in range(1, n):
            turn += idx[i] < idx[i-1]
            res += turn
        return res
