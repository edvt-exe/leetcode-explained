class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(s):
            count = 0

            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        result = []
        min_remove = len(s)

        def backtrack(i, current, removed):
            nonlocal min_remove

            if i == len(s):
                if valid(current):
                    if removed < min_remove:
                        result.clear()
                        min_remove = removed
                        result.append(current)
                    elif removed == min_remove:
                        if current not in result:
                            result.append(current)
                return
                
            backtrack(i + 1, current + s[i], removed)

            if s[i] == '(' or s[i] == ')':
                backtrack(i + 1, current, removed + 1)

        backtrack(0, "", 0)

        return result