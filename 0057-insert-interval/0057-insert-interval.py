class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []

        for interv in intervals:
            if interv[1] < newInterval[0]:
                ret.append(interv)
            elif interv[0] > newInterval[1]:
                ret.append(newInterval)
                newInterval = interv
            else:
                newInterval[0] = min(newInterval[0], interv[0])
                newInterval[1] = max(newInterval[1], interv[1])

        ret.append(newInterval)

        return ret