from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS,COLUMNS=len(grid),len(grid[0])
        res=[[float('inf')] * (COLUMNS+1) for _ in range(ROWS+1)]
        res[ROWS-1][COLUMNS]=0

        for r in range(ROWS-1,-1,-1):
            for c in range(COLUMNS-1,-1,-1):
                res[r][c]=grid[r][c]+min(res[r+1][c],res[r][c+1])
        
        return res[0][0] #as it is bottom up approach so we are returning the starting index

n=Solution()
grid=[[1,3,1],[1,5,1],[4,2,1]]
print(n.minPathSum(grid)) 