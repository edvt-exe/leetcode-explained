class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}

        if len(s) != len(t):
            return False

        for l in s:
            if l in s_letters:
                s_letters[l] += 1
            else:
                s_letters[l] = 1
        
        for l in t:
            if l in t_letters:
                t_letters[l] += 1
            else:
                t_letters[l] = 1

        if s_letters == t_letters:
            return True
        return False