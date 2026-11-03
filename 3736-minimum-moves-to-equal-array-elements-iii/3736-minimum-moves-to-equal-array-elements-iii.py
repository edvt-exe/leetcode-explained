class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx = max(nums)
        cnt = 0
        for i in nums:
            cnt += (maxx - i)

        return cnt