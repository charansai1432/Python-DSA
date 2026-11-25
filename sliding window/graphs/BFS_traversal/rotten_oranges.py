


# BFS approach 

def rotten_oranges(grid):
    
    minutes = 0
    fresh = 0 
    
    from collections import deque 
    queue = deque()
    
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append((row,col))
                
            elif grid[row][col] == 1:
                fresh += 1 
    
    while queue and fresh > 0:
        for i in range(len(queue)):
            cur_row,cur_col = queue.popleft()
            for dr,dc in directions:
                new_row = dr + cur_row
                new_col = dc + cur_col
            
                if 0 <= new_row < rows and 0 <= new_col < cols   and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.append((new_row,new_col))
                    
        
        minutes += 1 
    if fresh >0 : return -1 
    return minutes
print(rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]))