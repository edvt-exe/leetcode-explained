class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free_servers)
        
        busy_servers = []
        res = []
        curr_time = 0
        
        for j, task_duration in enumerate(tasks):
            curr_time = max(curr_time, j)
            
            while busy_servers and busy_servers[0][0] <= curr_time:
                _, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            if not free_servers:
                curr_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= curr_time:
                    _, weight, idx = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, idx))
            
            weight, idx = heapq.heappop(free_servers)
            res.append(idx)
            heapq.heappush(busy_servers, (curr_time + task_duration, weight, idx))
            
        return res