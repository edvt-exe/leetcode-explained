class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        ret_length = 0

        s_length = len(s)
        for i in range(s_length):
            l = i
            r = i
            while l >= 0 and r < s_length and s[l] == s[r]:
                if (r - l + 1) > ret_length:
                    ret = s[l:r + 1]
                    ret_length = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < s_length and s[l] == s[r]:
                if (r - l + 1) > ret_length:
                    ret = s[l:r + 1]
                    ret_length = r - l + 1
                l -= 1
                r += 1

        return ret