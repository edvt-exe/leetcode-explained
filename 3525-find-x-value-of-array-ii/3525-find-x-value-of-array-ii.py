class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            product_left, count_left = left
            product_right, count_right = right
            product = (product_left * product_right) % k
            count = count_left[:]
            for r in range(k):
                new_r = (product_left * r) % k
                count[new_r] += count_right[r]

            return [product, count]

        def build(node, left, right):
            if left == right:
                value = nums[left] % k

                tree[node][0] = value
                tree[node][1][value] = 1

                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, value):
            if left == right:
                value %= k

                tree[node][0] = value
                tree[node][1] = [0] * k
                tree[node][1][value] = 1

                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, right, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2
            if qr <= mid:
                return query(node * 2, left, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql, qr)
            left_result = query(node * 2, left, mid, ql, qr)
            right_result = query(node * 2 + 1, mid + 1, right, ql, qr)

            return merge(left_result, right_result)

        build(1, 0, n - 1)

        answer = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            result = query(1, 0, n - 1, start, n - 1)

            answer.append(result[1][x])

        return answer