class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        while prefix:
            nr = 0
            for word in strs:
                if word.startswith(prefix):
                    nr += 1
            if nr == len(strs):
                return prefix
            prefix = prefix[:-1]
        
        return ""