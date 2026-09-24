class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(c) for c in str(n))

        for i, x in enumerate(nums):
            if i == digit_sum(x):
                return i

        return -1