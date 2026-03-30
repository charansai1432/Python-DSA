#  “Given an integer array, find the contiguous subarray with the maximum sum and return that sum.”

# Constraints:

# 1 ≤ n ≤ 10^5
# -10^4 ≤ arr[i] ≤ 10^4

# Example:

# Input:  [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


#brute force approach

def maximum_sum_subarray(arr):
    max_sum = -1
    cur_sum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            cur_sum = sum(arr[i:j+1])
            # cur_sum = max(arr[i],cur_sum+arr[i])
            max_sum = max(cur_sum,max_sum)
            
    return max_sum
print(maximum_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))  


#optimal solution 

def maximum_sum_subarray(arr):
    
    max_sum = -1
    cur_sum = 0
    for i in arr:
        cur_sum = max(i,i+cur_sum)          #kadane algo 
        max_sum = max(max_sum,cur_sum)
    return max_sum
print(maximum_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))