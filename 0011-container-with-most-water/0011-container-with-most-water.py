class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        height_length = len(height)
        right = height_length - 1

        maximum = 0
        while left < right:
            width = right - left
            minim_height = min(height[left], height[right])

            curr = width * minim_height
            if curr > maximum:
                maximum = curr
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            
        return maximum