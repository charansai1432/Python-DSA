
# BFS approach 

def max_area_in_islands(grid):
    max_area = 0 
    rows = len(grid)
    cols = len(grid[0])
    
    visited = set()
    from collections import deque
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    area = 0 
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row,col)  not in visited:
                area = 0  
                queue = deque()
                queue.append((row,col))
                visited.add((row,col))
                while queue:
                    cur_row,cur_col = queue.popleft()
                    area += 1
                    for dr,dc in directions:
                        new_row = dr + cur_row 
                        new_col = dc + cur_col 
                        
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and  (new_row,new_col) not in visited:
                            queue.append((new_row,new_col))
                            visited.add((new_row,new_col))
                max_area = max(max_area,area)
    return max_area
                    
print(max_area_in_islands(grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
                                [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))


# dfs approach 

def max_area_in_island(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    max_area = 0 
    visited = set()
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    
    def dfs(row,col):
        nonlocal area 
        visited.add((row,col))
        area += 1 
        for dr,dc in directions:
            new_row = dr + row 
            new_col = dc + col  
            
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and (new_row,new_col) not in visited:
                dfs(new_row,new_col)
        
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row,col) not in visited:
                area = 0 
                dfs(row,col)
                max_area = max(max_area,area)
    return max_area
print(max_area_in_island(grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
                               [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
                               [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                               [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    
    
    