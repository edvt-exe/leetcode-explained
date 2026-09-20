class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []

        for i in range(len(words)):
            if not result or groups[i] != groups[i - 1]:
                result.append(words[i])

        return result