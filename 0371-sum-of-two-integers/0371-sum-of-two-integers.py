class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0XFFFFFFFF
        max_int = 0X7FFFFFFF

        while b!= 0:
            carry  = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= max_int:
            return a

        return ~(a ^ mask)