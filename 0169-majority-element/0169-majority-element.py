class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        count = 0

        for curr in nums:
            if count == 0:
                candidate = curr
            
            if candidate == curr:
                count += 1
            else:
                count -= 1
        
        return candidate