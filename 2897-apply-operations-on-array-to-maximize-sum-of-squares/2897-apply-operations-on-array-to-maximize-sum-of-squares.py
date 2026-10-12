class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7

        cnt = [0] * 31

        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    cnt[i] += 1

        ret = 0

        for _ in range(k):
            x = 0

            for i in range(31):
                if cnt[i] > 0:
                    x += 1 << i
                    cnt[i] -= 1

            ret = (ret + x * x) % mod

        return ret