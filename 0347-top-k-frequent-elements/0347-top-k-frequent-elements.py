class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        pairs = []
        for nr, nr_app in freq.items():
            pairs.append((nr_app, nr))

        pairs.sort(reverse=True)

        ret = []
        for i in range(k):
            ret.append(pairs[i][1])

        return ret