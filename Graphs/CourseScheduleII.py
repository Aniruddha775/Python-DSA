from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        g=defaultdict(list)

        for a,b in prerequisites:
            g[a].append(b)
        
        UNVISITED,VISITING,VISITED=0,1,2

        states=[UNVISITED]*numCourses

        def dfs(i):
            if states[i]==VISITED:
                return True
            elif states[i]==VISITING:
                return False
            states[i]=VISITING
            for nei_node in g[i]:
                if not dfs(nei_node):
                    return False
            
            states[i]=VISITED
            order.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order

n=Solution()
print(n.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) 