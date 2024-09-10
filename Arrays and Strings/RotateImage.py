from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        #Transpose
        #swap i and j
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        #Reflection of it
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]

n=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]    
n.rotate(matrix)
print(matrix)
