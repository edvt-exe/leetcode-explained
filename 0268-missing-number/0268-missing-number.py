class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nr = len(nums)
        gauss_sum = (nr * (nr + 1)) // 2
        nums_sum = sum(nums)
        ret = gauss_sum - nums_sum
        return ret