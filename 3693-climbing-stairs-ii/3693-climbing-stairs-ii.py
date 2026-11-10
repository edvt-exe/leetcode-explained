class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        inf = float('inf')
        f = [inf] * (n + 1)
        f[0] = 0
        
        for i in range(1, n + 1):
            cost_i = costs[i - 1]
            for j in range(max(0, i - 3), i):
                f[i] = min(f[i], f[j] + cost_i + (i - j) ** 2)
                
        return f[n]