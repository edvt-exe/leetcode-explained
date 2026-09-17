class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ogl = 0
        temp = x
        while temp:
            ogl = ogl * 10 + temp % 10
            temp //= 10
        if ogl == x:
            return True
        return False