# brute force approach 

def longest_subarray_with_sum_lessthan_k(arr,k):
    max_len = 0
    
    n = len(arr)
    
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum <= k:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_subarray_with_sum_lessthan_k([2,2,-1],3))


# here the optimal solution we have to solve this question using the prefix + Binary search + kadane's algo 

# the TC=> O(n log n ) due to binary search 
import bisect
def longest_subarray_with_sum_lessthan_eq_k(arr,k):
    
    prefix = 0
    max_len = 0
    
    sorted_prefix = [(0,-1)]            # storing the prefix_sum to index position in sorted_prefix
    
    for i , num in enumerate(arr):      # Get the index and number from the array
        prefix += num 
        
        target = prefix - k             # same as the maximum sum subarray of sum <= k 
                                        # in simple terms minimum prefix we need == target 
                                        
                                        
        for p,idx in sorted_prefix:     # find first_prefix >= target
            if p >= target:
                max_len = max(max_len,i-idx)        #length = current index - previous index 
                break                         #why break ??        # sorted_prefix is sorted i.e first_valid_prefix is found == best choice
        
        bisect.insort(sorted_prefix,(prefix,i))             # store current prefix + index in the sorted_prefix 
    return max_len
print(longest_subarray_with_sum_lessthan_eq_k([2,2,-1],3))
        
