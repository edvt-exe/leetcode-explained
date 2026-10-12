class Solution:
    def isHappy(self, n: int) -> bool:
        def calc_sq_digits(nr):
            ret = 0
            while nr:
                ret += (nr%10)*(nr%10)
                nr //= 10

            return ret
        
        seen = set()
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = calc_sq_digits(n)

