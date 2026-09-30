class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        map1 = {}
        map2 = {}

        for a, b in zip(pattern, words):
            if a in map1 and map1[a] != b:
                return False

            if b in map2 and map2[b] != a:
                return False

            map1[a] = b
            map2[b] = a

        return True