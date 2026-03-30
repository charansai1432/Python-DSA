# Q3. Maximum Subarray Sum (All Negative Case)

# 👉 “Return max subarray sum even if all elements are negative.”

# Example:
# Input:  [-3,-2,-5,-1]
# Output: -1
# Hint:
# Why max_sum = -inf matters


#brute force approach

def maximum_sum_subarray_all_neg_elements(arr):
    
    max_sum = -1
    # cur_sum = 0
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum = sum(arr[i:j+1])
            max_sum = max(max_sum,cur_sum)
    return max_sum
print(maximum_sum_subarray_all_neg_elements([-3,-2,-5,-1]))     #-1



# optimal apprach

def maximum_sum_subarray_all_neg_elements(arr):
    n = len(arr)
    cur_sum = 0 
    max_sum = -1
    for i in arr:
        cur_sum = max(i,cur_sum+i)
        max_sum = max(max_sum,cur_sum)
    return max_sum
print(maximum_sum_subarray_all_neg_elements([-3,-2,-5,-1]))     #-1