'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

def exist(board, word):
    ROWS,COLS = len(board), len(board[0])
    pos = set()
    
    def dfs(z, i,j):
        
        if z == len(word):
            return True
        if i >= ROWS or j >= COLS or i < 0 or j < 0 or (i,j) in pos or board[i][j] != word[z]:
            return False
        pos.add((i,j))

        res = dfs(z+1,i-1,j) or dfs(z+1, i+1,j) or dfs(z+1, i,j-1)or dfs(z+1, i,j+1)
        pos.remove((i,j))

        return res

    for i in range(ROWS):
        for j in range(COLS):
            if dfs(0,i,j):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
answer = exist(board,word)
print(answer)