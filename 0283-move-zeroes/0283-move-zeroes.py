class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = 0
        index = 0
        
        while index < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                ct += 1
            else:
                index += 1

        while ct:
            nums.append(0)
            ct -= 1

        


        