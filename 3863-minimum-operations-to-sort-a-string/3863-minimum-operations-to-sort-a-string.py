class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        minn = min(s)
        maxx = max(s)

        if s == ''.join(sorted(s)):
            return 0

        if s[0] == minn or s[-1] == maxx:
            return 1

        if minn in s[:-1] or maxx in s[1:]:
            return 2

        if n == 2:
            return -1

        return 3