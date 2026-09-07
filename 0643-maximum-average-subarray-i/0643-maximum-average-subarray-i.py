class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        nums_length = len(nums)
        for i in range (k, nums_length):
            curr_sum = curr_sum + nums[i] - nums[i- k]

            if curr_sum > max_sum:
                max_sum = curr_sum

        ret = max_sum / k
        return ret