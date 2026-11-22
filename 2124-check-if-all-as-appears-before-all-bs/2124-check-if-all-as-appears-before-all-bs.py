class Solution:
    def checkString(self, s: str) -> bool:
        okB = 0
        for i in s:
            if i == 'a' and okB == 1:
                return False
            if i == 'b':
                okB = 1
        return True

