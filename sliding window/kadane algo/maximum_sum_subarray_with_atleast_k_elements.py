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
    
    
# optimal solution (NOT DONE THIS QUESTION OPTIMAL ONE)

def maximum_sum_subarray_atleast_k_elements(arr,k):
    n = len(arr)
    
    # Step 1: Kadane till each index
    max_end = [0]*n
    curr = arr[0]
    max_end[0] = arr[0]
    
    for i in range(1, n):
        curr = max(arr[i], curr + arr[i])
        max_end[i] = curr
    
    # Step 2: window of size k
    window_sum = sum(arr[:k])
    ans = window_sum
    
    for i in range(k, n):
        window_sum += arr[i] - arr[i-k]
        
        # extend using Kadane
        ans = max(ans, window_sum + max_end[i-k], window_sum)
    return ans
print(maximum_sum_subarray_atleast_k_elements([1,2,3,-10,4,5],2))
