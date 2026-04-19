# “Find max sum of subarray having size ≥ k.”

# Constraints:
# 1 ≤ k ≤ n

# Example:
# Input: arr = [1,2,3,-10,4,5], k = 2
# Output: 9

# Hint:
# sliding window of size k
# extend using Kadane (prefix idea)

# Here this question is kadane + prefix because

# Subarray size must be ≥ k ==> this is the logic to became prefix pattern


# brute force approach

def maximum_sum_subarray_atleast_k_elements(arr,k):
    n = len(arr)
    max_sum = -1
    for i in range(n):
        w_sum = 0
        for j in range(i,n):
            w_sum += arr[j]
            if (j-i+1) >= k:
                max_sum = max(max_sum,w_sum)
    return max_sum
print(maximum_sum_subarray_atleast_k_elements([1,2,3,-10,4,5],2))  #9
    

# This question is solved using the prefix sum + kadane's algo question 

# here the main logic is 1st we compute the k size max_sum after that we extend backward to get max_sum 

# after calculating the k size of max_sum ==> we think like if i extend backward can i get the max_sum this logic is done by the kadane's algo



# optimal solution 

def maximum_sum_subarray_atleast_k_elements(arr,k):       # (THIS IS QUESTION IS SOLVED USING THE PREFIX SUM + KADANE'S ALGO)
    n = len(arr)
    
    max_sum_ending_index = [0]*n                #  created the prefix array 
    max_sum_ending_index[0] = arr[0]
    
    # Step 1: Kadane PRE-COMPUTE
    # max_sum_ending_here[i] = best subarray sum ending at index i
    
    for i in range(1,n):
        max_sum_ending_index[i] = max(arr[i] , arr[i] + max_sum_ending_index[i-1])          # creating the prefix sum array along with the kadane's logic i.e in the kadane's max_sum_subarray question the we return something like max(num,cur_sum+num)
        
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Get the window_sum of the k size 
    
    for i in range(k,n):
        window_sum += arr[i] - arr[i-k]
        
        # Option 1: take only k elements
        max_sum = max(max_sum,window_sum)
        
        
        # Option 2: extend backward using Kadane
        max_sum = max(max_sum , window_sum + max_sum_ending_index[i-k])
        
        
    return max_sum
print(maximum_sum_subarray_atleast_k_elements([1,2,3,-10,4,5],2))
