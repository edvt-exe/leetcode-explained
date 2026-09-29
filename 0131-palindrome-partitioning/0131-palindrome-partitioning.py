class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []

        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start, len(s)):
                part = s[start:end + 1]

                if part == part[::-1]:
                    current.append(part)
                    backtrack(end + 1, current)
                    current.pop()

        backtrack(0, [])

        return result