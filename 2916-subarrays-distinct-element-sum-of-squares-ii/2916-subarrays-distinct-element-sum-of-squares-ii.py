class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        seg_sum = [0] * (4 * n)
        seg_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node: int, left: int, right: int, delta: int) -> None:
            length = right - left + 1
            old_sum = seg_sum[node]
            seg_sq[node] = (seg_sq[node] + 2 * delta * old_sum + length * delta * delta) % MOD
            seg_sum[node] = (old_sum + length * delta) % MOD

            lazy[node] += delta

        def push(node: int, left: int, right: int) -> None:
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            delta = lazy[node]

            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)
            lazy[node] = 0

        def update(node: int, left: int, right: int, ql: int, qr: int) -> None:
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            seg_sum[node] = (seg_sum[node * 2] + seg_sum[node * 2 + 1]) % MOD
            seg_sq[node] = (seg_sq[node * 2] + seg_sq[node * 2 + 1]) % MOD

        last_seen = {}
        answer = 0

        for i, x in enumerate(nums):
            previous = last_seen.get(x, -1)
            update(1, 0, n - 1, previous + 1, i)
            answer = (answer + seg_sq[1]) % MOD
            last_seen[x] = i

        return answer