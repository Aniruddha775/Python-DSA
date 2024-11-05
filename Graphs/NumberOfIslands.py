from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return
            else:
                grid[i][j]='0' #marking it 0 so that we dont visit it again
                dfs(i,j+1) #go right
                dfs(i+1,j) #go bottom
                dfs(i,j-1) #go left
                dfs(i-1,j) #go top
        

        num_island=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    num_island+=1
                    dfs(i,j)
        
        return num_island

n=Solution()
print(n.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
