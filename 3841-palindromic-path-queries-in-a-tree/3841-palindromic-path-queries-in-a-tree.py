class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        LOG = n.bit_length()

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [0] * n
        pref = [0] * n

        timer = 0
        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                depth[u] = 0 if u == p else depth[p] + 1

                b = 1 << (ord(s[u]) - 97)
                pref[u] = b if u == p else pref[p] ^ b

                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        up = [parent[:]]

        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]
            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def get(i):
            res = 0
            i += 1

            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def update(l, r, val):
            add(l, val)
            if r + 1 < n:
                add(r + 1, val)

        def get_prefix(u):
            return pref[u] ^ get(tin[u])

        chars = list(s)
        ans = []
        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = ((1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97)))

                if delta:
                    update(tin[u], tout[u], delta)

                chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                mask = (get_prefix(u) ^ get_prefix(v) ^ (1 << (ord(chars[w]) - 97)))

                ans.append(mask & (mask - 1) == 0)

        return ans
