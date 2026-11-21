class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = defaultdict(list)
        
        def dfs_reparent(u: int) -> None:
            char = s[u]
            if last_seen[char]:
                new_parent[u] = last_seen[char][-1]
                
            last_seen[char].append(u)
            for v in adj[u]:
                dfs_reparent(v)
            last_seen[char].pop()
            
        dfs_reparent(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def dfs_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += dfs_size(v)
            return ans[u]
            
        dfs_size(0)
        return ans