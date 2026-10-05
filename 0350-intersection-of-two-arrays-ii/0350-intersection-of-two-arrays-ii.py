class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        v1 = [0] * 1001
        v2 = [0] * 1001
        ret = []

        for i in nums1:
            v1[i] += 1

        for i in nums2:
            v2[i] += 1

        for i in range(1001):
            if v1[i] and v2[i]:
                for _ in range(min(v1[i], v2[i])):
                    ret.append(i)

        return ret