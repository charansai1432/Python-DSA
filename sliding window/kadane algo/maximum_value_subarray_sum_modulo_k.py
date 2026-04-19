# This question is a maximum sum subarray => kadane's + prefix sum question 

# Here in this question we are returning the max_val in a sub array when the sum%k is valid 
# Here we aren't returning the max_sum or anything (IMPORTANT)

# brute force approach 

def maximum_subarray_sum_modulo_k(arr,k):
    max_sum = float('-inf')
    for i in range(len(arr)):
        cur_sum = 0
        for j in range(i,len(arr)):
            cur_sum += arr[j]
            
            max_sum = max(max_sum,cur_sum%k)
    return max_sum
print(maximum_subarray_sum_modulo_k([3,3,9,9,5],7))


# the time complexity is TC=> O(n log n)

# optimal solution approach
import bisect
def maximum_value_subarray_sum_modulo_k(arr,k):
    prefix = 0
    n = len(arr)
    sorted_prefix = [0]
    max_val = 0                                 # we can also assume here prefix = cur_prefix
                                                # previous prefix are stored in the sorted_prefix
    for i in range(n):
        
        prefix = (prefix+arr[i])%k
        
        idx = bisect.bisect_right(sorted_prefix,prefix)
        
        if idx < len(sorted_prefix):
            max_val = max(max_val,prefix-sorted_prefix[idx]+k)
            
        else:
            max_val =  max(max_val,prefix)                  # There is NO previous prefix that is strictly greater than current prefix
            
        bisect.insort(sorted_prefix,prefix)
        
    return max_val

print(maximum_value_subarray_sum_modulo_k([3,3,9,9,5],7))


# Why wrap-around fails here

# Remember:

# (prefix[j] - prefix[i] + k)

# 👉 This only gives big value when:

# prefix[i] > prefix[j]

# 👉 But here:

# no prefix[i] > prefix[j]

# 👉 So no wrap-around possible ❌