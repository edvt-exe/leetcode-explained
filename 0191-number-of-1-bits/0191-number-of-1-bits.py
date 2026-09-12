class Solution:
    def hammingWeight(self, n: int) -> int:
        nr = 0
        while n:
            n = n & (n - 1)
            nr += 1
        return nr