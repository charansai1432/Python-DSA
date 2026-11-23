
# BFS approach 

def no_of_islands(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    
    from collections import deque
    queue = deque()
    visited = set()
    islands = 0
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row,col) not in visited:
                islands += 1 
                
                queue.append((row,col))
                while queue:
                    cur_row ,cur_col = queue.popleft()
                    for dr,dc in directions:
                        new_row = cur_row + dr 
                        new_col = cur_col + dc 
                        
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1" and (new_row,new_col) not in visited:
                            queue.append((new_row,new_col))
                            visited.add((new_row,new_col))
    return islands
    
    
print(no_of_islands(grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))



# DFS approach 

def no_of_island(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    islands = 0 
    visited = set()
    
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    def dfs(row,col):
        
        visited.add((row,col))
        
        for dr,dc in directions:
            new_row = dr + row 
            new_col =dc + col 
            
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1" and (new_row,new_col) not in visited:
                dfs(new_row,new_col)
       
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row,col) not in visited:
                islands += 1 
                dfs(row,col)
    return islands
print(no_of_island(grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
    
    
    