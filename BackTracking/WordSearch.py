from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        W = len(word)

        if m == 1 and n == 1:
            return board[0][0] == word

        def backtrack(pos, index):
            i, j = pos

            if index == W:
                return True

            if board[i][j] != word[index]:
                return False

            char = board[i][j] #temporary storing the value for future usage
            board[i][j] = "#" #we marking it with '#' so that we dont visit it again

            for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = i + i_off, j + j_off

                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r, c), index + 1):
                        return True

            board[i][j] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack((i, j), 0):
                    return True

        return False

board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCCED"
s = Solution()
print(s.exist(board, word)) 