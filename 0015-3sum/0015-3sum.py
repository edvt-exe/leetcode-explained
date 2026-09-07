class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []

        nums.sort()
        nums_length = len(nums)
        for i in range(nums_length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = nums_length - 1

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])

                    # skip the duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ret
