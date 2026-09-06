class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        list_length = len(nums)
        for i in range(list_length):
            curr = nums[i]
            nr = target - curr
            if nr in visited:
                return [visited[nr], i]

            visited[curr] = i

        return []