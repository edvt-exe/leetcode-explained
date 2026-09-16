class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        nr = 0

        for i in range(n):
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                nr += 1
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                nr += 1
                left -= 1
                right += 1

        return nr