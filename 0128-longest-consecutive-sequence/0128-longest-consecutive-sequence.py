class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nr = set(nums)
        seq_max = 0

        for i in nr:
            if (i - 1) not in nr:
                curr_length = 1
                curr = i

                while (curr + 1) in nr:
                    curr += 1
                    curr_length += 1

                if curr_length > seq_max:
                    seq_max = curr_length

        return seq_max