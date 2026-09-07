class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(c):
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                return True
            return False
        s_length = len(s)
        left = 0
        right = s_length - 1

        while left < right:
            while left < right and not is_alphanumeric(s[left]):
                left += 1

            while left < right and not is_alphanumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
            