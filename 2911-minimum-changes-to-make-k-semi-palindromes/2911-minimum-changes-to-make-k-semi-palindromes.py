class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    for r in range(d):
                        left = r
                        right = length - d + r

                        while left < right:
                            if s[i + left] != s[i + right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(1, n + 1):

                for j in range(parts - 1, i):
                    if i - j < 2:
                        continue

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i - 1]
                    )

        return dp[n][k]