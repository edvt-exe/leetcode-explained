class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(n + 1):
            nr = 0
            curr = i
            while curr:
                curr = curr & ( curr - 1)
                nr += 1
            ret.append(nr)
        return ret