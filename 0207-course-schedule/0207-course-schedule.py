class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for c, prev in prerequisites:
            adj[prev].append(c)
            in_degree[c] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while queue:
            node = queue.popleft()
            completed += 1
            for neigh in adj[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        return completed == numCourses