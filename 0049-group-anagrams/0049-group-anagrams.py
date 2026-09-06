class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            freq = [0] * 26
            for l in s:
                pos = ord(l) - ord('a')
                freq[pos] += 1

            key = tuple(freq)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        groups_list = list(groups.values())
        return groups_list