class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                ret += len(distinct) ** 2

        return ret