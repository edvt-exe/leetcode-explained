class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 1315423911, 2654435761
        
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        
        for i in range(n):
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2
            val = nums[i] + 1
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2
            
        def has_unique(length: int) -> bool:
            p1, p2 = pow1[length], pow2[length]
            counts = Counter()
            for i in range(n - length + 1):
                h1 = (pref1[i + length] - pref1[i] * p1) % MOD1
                h2 = (pref2[i + length] - pref2[i] * p2) % MOD2
                counts[(h1, h2)] += 1
            return 1 in counts.values()
            
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if has_unique(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans