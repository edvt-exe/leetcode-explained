class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def solve(nums):
            if len(nums) <= 2:
                return 1

            root = nums[0]

            left = [x for x in nums if x < root]
            right = [x for x in nums if x > root]

            ways = comb(len(left) + len(right), len(left))

            return ways * solve(left) * solve(right) % MOD

        return (solve(nums) - 1) % MOD