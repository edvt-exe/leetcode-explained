class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        max_length = 0

        s_length = len(s)
        for i in range(s_length):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[i])
            curr = i - left + 1
            if curr > max_length:
                max_length = curr

        return max_length