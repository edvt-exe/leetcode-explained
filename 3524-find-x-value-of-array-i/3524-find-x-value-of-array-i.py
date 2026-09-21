class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        prev = [0] * k

        for num in nums:
            x = num % k
            curr = [0] * k

            curr[x] += 1

            for r in range(k):
                if prev[r]:
                    curr[(r * x) % k] += prev[r]

            for r in range(k):
                ans[r] += curr[r]

            prev = curr

        return ans