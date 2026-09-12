class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        curr = 0

        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            if max_subarray < curr:
                max_subarray = curr
        
        return max_subarray