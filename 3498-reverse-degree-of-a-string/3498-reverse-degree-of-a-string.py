class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, char in enumerate(s):
            value = ord('z') - ord(char) + 1
            total += value * (i + 1)

        return total