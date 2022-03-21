# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board, word):
        # board = m x n matrix
        m = len(board)
        n = len(board[0])
        # print(m, n)
        
        # check whether can find word, start at (i,j) position    
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        # print(board, i, j, word)
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        
        # 🔑 check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
            or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        
        board[i][j] = tmp # 🔑 avoids the danger of 'going back' problem.
        return res
