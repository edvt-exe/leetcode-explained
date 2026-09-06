class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nr = len(nums)

        nums1 = [1] * nr
        nums2 = [1] * nr
        ret = [1] * nr

        for i in range(1, nr):
            nums1[i] = nums1[i-1] * nums[i - 1]
        
        for i in range (nr - 2, -1, -1):
            nums2[i] = nums2[i + 1] * nums[i + 1]

        for i in range(nr):
            ret[i] = nums1[i] * nums2[i]

        return ret