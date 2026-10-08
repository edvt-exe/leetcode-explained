class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ret = ""

        for i in s:
            if i == "(":
                cnt += 1
                if cnt > 1:
                    ret += "("
            else:
                cnt -= 1
                if cnt > 0:
                    ret += ")"

        return ret
        
            