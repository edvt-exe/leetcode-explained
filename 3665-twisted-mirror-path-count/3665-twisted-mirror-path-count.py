class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        D = [0] * n
        ways = 0
        
        for i in range(m):
            current_R = 0 
            
            for j in range(n):
                if i == 0 and j == 0:
                    out_R = 1
                    out_D = 1
                    ways = 1
                else:
                    R_in = current_R
                    D_in = D[j]
                    
                    if grid[i][j] == 0:
                        ways = (R_in + D_in) % MOD
                        out_R = ways
                        out_D = ways
                    else:
                        out_R = D_in  
                        out_D = R_in  
                        
                current_R = out_R
                D[j] = out_D
                
        return ways