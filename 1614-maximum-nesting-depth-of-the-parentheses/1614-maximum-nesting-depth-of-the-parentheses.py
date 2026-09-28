class Solution:
    def maxDepth(self, s: str) -> int:
        nrmax = 0

        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
                if cnt > nrmax:
                    nrmax = cnt
            if c == ')':
                cnt -= 1
        
        return nrmax