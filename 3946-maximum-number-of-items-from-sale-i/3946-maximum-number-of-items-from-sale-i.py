class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        freq = Counter(f for f, _ in items)
        
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            for mult in range(f, max_factor + 1, f):
                multiples_count[f] += freq[mult]
                
        dp = [0] * (budget + 1)
        for factor, price in items:
            value = multiples_count[factor]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + value > dp[b]:
                    dp[b] = dp[b - price] + value
                    
        min_price = min(p for _, p in items)
        for b in range(min_price, budget + 1):
            if dp[b - min_price] + 1 > dp[b]:
                dp[b] = dp[b - min_price] + 1
                
        return max(dp)