class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[0] = True

        for i in range(1, s_len + 1):
            for word in wordDict:
                if i >= len(word):
                    if dp[i- len(word)] and s[i - len(word) : i] == word:
                        dp[i] = True
                        break

        return dp[s_len]