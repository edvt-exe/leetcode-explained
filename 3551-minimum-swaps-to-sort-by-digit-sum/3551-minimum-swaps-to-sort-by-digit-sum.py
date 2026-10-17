class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        arr = sorted((digit_sum(x), x, i) for i, x in enumerate(nums))
        perm = [item[2] for item in arr]

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or perm[i] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = perm[j]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
