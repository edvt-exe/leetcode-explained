class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_helper(houses):
            prev = 0
            curr = 0
            for money in houses:
                new_curr = max(curr, prev + money)
                prev = curr
                curr = new_curr
            return curr
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))