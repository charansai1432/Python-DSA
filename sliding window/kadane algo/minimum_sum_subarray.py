# Find the contiguous subarray with the minimum possible sum.”

# Constraints:

# Same as above

# Example:
# Input:  [3,-4,2,-3,-1,7,-5]
# Output: -6


#brute force approach
def minimum_sum_subarray(arr):
    min_sum =0
    cur_sum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            cur_sum = sum(arr[i:j+1])
            min_sum = min(min_sum,cur_sum)
    return min_sum
print(minimum_sum_subarray([3,-4,2,-3,-1,7,-5]))    #-6


#optimal approach

def minimum_sum_subarray(arr):
    min_sum = 0
    
    cur_sum = 0
    for i in arr:
        cur_sum = min(i,cur_sum+i)
        min_sum = min(cur_sum,min_sum)
    return min_sum
print(minimum_sum_subarray([3,-4,2,-3,-1,7,-5]))    #-6