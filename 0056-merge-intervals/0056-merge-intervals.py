class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ret = []
        for interv in intervals:
            if not ret or ret[-1][1] < interv[0]:
                ret.append(interv)
            else:
                ret[-1][1] = max(ret[-1][1], interv[1])

        return ret