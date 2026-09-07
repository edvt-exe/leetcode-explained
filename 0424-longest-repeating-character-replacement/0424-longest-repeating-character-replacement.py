class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        s_length = len(s)
        right = s_length - 1

        freq = {}
        max_length = 0
        max_freq = 0

        for i in range(s_length):
            curr = s[i]
            freq[curr] = freq.get(curr, 0) + 1
            if max_freq < freq[curr]:
                max_freq = freq[curr]

            window_length = i - left + 1
            while window_length - max_freq > k:
                c1 = s[left]
                freq[c1] -= 1
                left += 1
                window_length = i - left + 1

            if window_length > max_length:
                max_length = window_length

        return max_length