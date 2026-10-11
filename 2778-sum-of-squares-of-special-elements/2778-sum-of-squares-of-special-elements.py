class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                ret += nums[i] * nums[i]
        
        return ret