'''
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. 
You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. 
If you cut the pizza vertically, give the left part of the pizza to a person. 
If you cut the pizza horizontally, give the upper part of the pizza to a person. 
Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. 
Since the answer can be a huge number, return this modulo 10^9 + 7.
'''

MOD = 10**9 + 7
    
def ways(self, pizza: List[str], k: int) -> int:
    

    m, n = len(pizza), len(pizza[0])
    apples = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            apples[i][j] = apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1] + (pizza[i][j] == 'A')
    
    dp = {}
    def solve(i, j, p):
        if (i, j, p) in dp:
            return dp[(i, j, p)]
        if p == 1:
            
            return 1 if apples[i][j] > 0 else 0
            
        ans = 0
        for r in range(i+1, m):
            if apples[i][j] - apples[r][j] > 0:
                ans = (ans + solve(r, j, p-1)) % self.MOD
        for c in range(j+1, n):
            if apples[i][j] - apples[i][c] > 0:
                ans = (ans + solve(i, c, p-1)) % self.MOD
        dp[(i, j, p)] = ans
        return ans

    return solve(0, 0, k)