class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        for i in range(26):
            if last[i] == -1:
                continue

            left = first[i]
            right = last[i]
            j = left
            valid = True

            while j <= right:
                idx = ord(s[j]) - ord('a')

                if first[idx] < left:
                    valid = False
                    break

                right = max(right, last[idx])
                j += 1

            if valid:
                intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for left, right in intervals:
            if left > end:
                result.append(s[left:right + 1])
                end = right

        return result