
# pattern recognition 

# Histogram Problem

# For every bar:

# Expand Left
# Expand Right
# Find Width
# Find Area
# Update Max Area



# cheat sheet 
    # In the question 1st we have to assume the minimum height 
    # calcuate the next smaller and previous smaller element 
    # width calculation 
    # area find out that's it 
    
# at every step we assume that this is the minimum_height 
# and move left side and right side 

# in the brute force approach for width calculation width = r - l + 1
# in the optimal solution approach the width calculation is widht => NSE - PSE - 1

# in the BF approach => l,r are valid bars that means in that we can find the max_area 

# in the optimal approach == > NSE & PSE are invalid bars ==> we have to exclude that 

# brute force approach 
def largest_rectangle_in_histogram(heights):
    n = len(heights)
    max_area = 0
    
    for i in range(n):
        
        cur_height = heights[i]
        # for the previoous smaller element find out 
        
        left = i                # from this index to left side we have to find previous smaller element 
        
        for j in range(i-1,-1,-1):
            
            if heights[j] >= cur_height:        # here we have to find out the until the previous smaller height 
               left = j     # until the previous smaller height find out iterate it 
            
            else:
                break
        
        # for the next smaller element find out 
            
        right = i           # from this index to right side we have to find the next smaller element 
        
        for j in range(i+1,n):      # forward moving this is the default condition refer the greater/smaller problems 
            
            if heights[j] >= cur_height:        # the min_height is cur_height because it's a next smaller element 
                right = j           # until the next smaller height find out iterate it 
            
            else:
                break
            
        width = right - left + 1
        
        area = width * cur_height
        
        max_area = max(max_area,area)
    return max_area
                
print(largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]))   #10


# optimal solution approach 

def largest_rectangle_in_histogram(heights):
    
    # previous smaller
    n = len(heights)
    stack = []
    pse = [-1]*n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
            
        if stack:
            pse[i] = stack[-1]
        stack.append(i)
        
    # next smaller 
    
    n = len(heights)
    stack = []          # 2 stacks must be defind here to avoid the values stored in the both NSE and pse if stored in the single stack it cause the calculation issue's 
    nse = [n]*n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            idx = stack.pop()
            nse[idx] = i
        stack.append(i)
        
    max_area = 0
    n = len(heights)
    for i in range(n):
        width = nse[i] - pse[i] - 1
        area = heights[i] * width
        max_area = max(max_area,area)
    return max_area
print(largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]))   #10
            