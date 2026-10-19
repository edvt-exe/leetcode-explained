class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ret = []

        for i in range(1, len(nums)+1):
            if nums[i-1] == target:
                ret.append(i-1)

        return ret
