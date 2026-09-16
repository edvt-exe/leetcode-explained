class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda v: v[1])
        nr = 0
        last_end = intervals[0][1]
        intervals_len = len(intervals)
        for i in range(1, intervals_len):
            if intervals[i][0] < last_end:
                nr += 1
            else:
                last_end = intervals[i][1]

        return nr