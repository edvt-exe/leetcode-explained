class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        suma = 0
        n = len(nums)

        for i in range(n):
            if i < n // 2:
                suma -= nums[i]
            else:
                suma += nums[i]

        return suma

