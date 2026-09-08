class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        nums_length = len(nums)
        right = nums_length - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]