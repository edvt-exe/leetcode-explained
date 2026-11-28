class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = Counter(f for f, _ in items)
        
        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for mult in range(f, n + 1, f):
                    multiples_count[f] += freq[mult]
                    
        min_price = min(p for _, p in items)
        
        bundles = []
        for factor, price in items:
            cap = multiples_count[factor] - 1
            if cap > 0 and price < 2 * min_price:
                bundles.append((price, cap))
                
        bundles.sort()
        
        best_items = budget // min_price
        spent = 0
        bundles_bought = 0
        
        for price, cap in bundles:
            if spent + price > budget:
                break
                
            can_take = min(cap, (budget - spent) // price)
            spent += can_take * price
            bundles_bought += can_take
            
            rem_budget = budget - spent
            total = bundles_bought * 2 + (rem_budget // min_price)
            if total > best_items:
                best_items = total
                
        return best_items