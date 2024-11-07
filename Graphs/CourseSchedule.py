from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses=prerequisites
        g=defaultdict(list)

        for a,b in courses: #building adjacency graph list
            g[a].append(b)
        
        UNVISITED=0
        VISITING=1
        VISITED=2

        states=[UNVISITED]*numCourses #marking all nodes as 0 at first

        def dfs(node):
            state=states[node]

            if state==VISITED: return True
            elif state==VISITING: return False
            for nei_node in g[node]:
                if not dfs(nei_node): #means it contains a cycle (VISITING STATE NOT VISITED STATE)
                    return False

            states[node]=VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False #means it contains a cycle
        
        return True

n=Solution()
print(n.canFinish(2, [[1,0]])) 

