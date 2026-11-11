class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost_individual = need1 * cost1 + need2 * cost2
        
        common = min(need1, need2)
        cost_mixed = common * costBoth + (need1 - common) * cost1 + (need2 - common) * cost2
        
        cost_combo_only = max(need1, need2) * costBoth
        
        return min(cost_individual, cost_mixed, cost_combo_only)