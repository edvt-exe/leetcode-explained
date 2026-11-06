class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        counts = defaultdict(int)

        left = 0
        right = 0

        result = [0] * len(queries)

        for q, idx in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                counts[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                counts[server] -= 1

                if counts[server] == 0:
                    del counts[server]

                left += 1

            result[idx] = n - len(counts)

        return result