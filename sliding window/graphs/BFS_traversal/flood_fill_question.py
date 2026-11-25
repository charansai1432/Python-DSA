


def flood_fill(image,sr,sc,color):
    
    from collections import deque
    
    queue = deque()
    original_color = image[sr][sc]
    
    queue.append((sr,sc))
    
    # edge case 
    if image[sr][sc] == color:
        return image 
    
    image[sr][sc] = color 
    
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    
    rows = len(image)
    cols = len(image[0])
    
    while queue:
        cur_row,cur_col = queue.popleft()
        for dr,dc in directions:
            new_row = dr + cur_row
            new_col = dc + cur_col
            
            if 0<= new_row < rows and 0 <= new_col < cols and image[new_row][new_col] == original_color:
                image[new_row][new_col] = color
                queue.append((new_row,new_col))
    return image 

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1 
sc = 1 
color = 2


print(flood_fill(image,sr,sc,color))