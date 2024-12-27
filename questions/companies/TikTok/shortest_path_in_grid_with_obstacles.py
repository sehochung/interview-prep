import collections
def shortestPath(grid, k: int) -> int:
    ROWS,COLS = len(grid), len(grid[0])

    # up, down, left,right
    directions = [ [-1,0],[0,-1],[1,0],[0,1] ]

    positions = set()
    queue = collections.deque([(0,(0,0,k))])
    while queue:
        steps, position = queue.popleft()
        
        if position[0] == ROWS-1 and position[1] == COLS-1:
            return steps

        for x,y in directions:
            if 0 <= position[0]+x < ROWS and 0 <= position[1]+y < COLS:
                new_row = position[0]+x
                new_col = position[1]+y
                new_k = position[2]-grid[new_row][new_col]
                if new_k >= 0 and (new_row,new_col,new_k) not in positions:
                    positions.add((new_row,new_col,new_k))
                    queue.append((steps+1,(new_row, new_col, new_k)))

    return -1
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1

answer = shortestPath(grid,k)
print(answer)