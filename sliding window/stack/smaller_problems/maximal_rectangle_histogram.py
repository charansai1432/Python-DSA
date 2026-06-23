
# Maximal Rectangle Problem

# For every row:

# Build Histogram
# Run Histogram Algorithm
# Update Max Rectangle

# brute force approach 


def largest_rectangle_area(heights):
    n = len(heights)
    max_area = 0
    for i in range(n):
        cur_height = heights[i]
        left = i
        right = i
        for j in range(i-1,-1,-1):
            if heights[j] >= heights[i]:
                left = j 
            else:
                break 
        for j in range(i+1,n):
            if heights[j] >= heights[i]:
                right = j
            else:
                break
        width = right - left + 1
        area = width*cur_height
        max_area = max(max_area,area)
    return max_area

def maximal_rectangle_histogram(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    heights = [0]* cols
    max_area = 0
    if not matrix:
        return 0 
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "1":
                heights[col] += 1
            else:
                heights[col] = 0
        print(f"{heights}")
        area = largest_rectangle_area(heights)
        max_area = max(max_area,area)
    return max_area
print(maximal_rectangle_histogram([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))             # 6 ==> T.C is O(R × C²)




# {VVVVIMP} Question 
# optimal solution approach 

def largest_rectangle_area(heights):
    n = len(heights)
    
    nse = [n] *n
    pse = [-1] * n
    stack = []
    max_area = 0
    # previous smaller element
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            pse[i] = stack[-1]
        stack.append(i)
        
    # next smaller element
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            idx = stack.pop()
            nse[idx] = i
        stack.append(i)
        
    # for calculating the every bar in the iteration and assuming the cur_height is minimum bar 
    for i in range(n):
        cur_height = heights[i]
        width = nse[i] - pse[i] - 1
        area = cur_height * width
        max_area = max(max_area,area)
        
    return max_area 

def  maximal_rectangle_histogram(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols
    n = len(matrix)
    max_area = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "1":
                heights[col] += 1
            else:
                heights[col] = 0 
        print(f"{heights}")
        
        area = largest_rectangle_area(heights)
        max_area = max(max_area,area)
    return max_area
print(maximal_rectangle_histogram([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))         # 6 ==> TC is O(R × C)


                
