from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1

        while l <= r:
            m = (l + r) // 2
            i = m // n #get the row index
            j = m % n #get the column index
            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1

        return False

n=Solution()
print(n.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))