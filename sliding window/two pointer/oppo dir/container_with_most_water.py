# “You’re given an array where each element represents the height of a vertical line. Choose two lines such that together they form a container that holds the maximum amount of water.”

# 🔍 Example
# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49

# brute force approach 

def container_with_most_water(heights):
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i+1,n):
            width = j - i
            min_height = min(heights[i],heights[j])
            area = width*min_height
            max_water = max(max_water,area)
    return max_water
print(container_with_most_water([1,8,6,2,5,4,8,3,7]))


# optimal approach 

def container_with_most_water(heights):
    n = len(heights)
    l = 0
    r = n - 1
    max_water = 0
    while l < r:
        width  = r - l 
        height = min(heights[l],heights[r])
        area = height * width
        max_water = max(max_water,area)
        
        if heights[l] < heights[r]:         # here we moving the small height only because imagine 1st like heights are lines right here 
                                                    # if we move the highest height forward to use --> why ?  --> current area is limited by smaller height, so we try to find a taller one by moving it
                                                    # so we have to move the small height okk so that we are doing the heights[l] == small height ... We move the smaller height because it is limiting the area
            l+=1
        else:
            r-=1
    return max_water
print(container_with_most_water([1,8,6,2,5,4,8,3,7]))