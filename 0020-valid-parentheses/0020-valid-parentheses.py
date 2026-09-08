class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        s_map = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }

        for c in s:
            if c in s_map:
                curr = '#'
                if stack:
                    curr = stack.pop()
                
                if s_map[c] != curr:
                    return False
            
            else:
                stack.append(c)

        return not stack