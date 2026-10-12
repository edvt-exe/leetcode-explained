class Solution:
    def addDigits(self, num: int) -> int:
        def calc_digits(nr):
            ret = 0
            while nr:
                ret += nr % 10
                nr //= 10

            return ret

        while num > 9:
            num = calc_digits(num)

        return num 