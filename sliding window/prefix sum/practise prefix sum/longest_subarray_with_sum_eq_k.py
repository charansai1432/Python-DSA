#brute force approach

def longest_subarray_with_sum_eq_k(arr,k):
    max_len = 0
    n = len(arr)
    # freq = {0:-1}
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum +=arr[j]
            
            if cur_sum == k:
                max_len = max(max_len,j-i+1)
            
    return max_len
print(longest_subarray_with_sum_eq_k([1,2,3,1,1,1],3))      #3

#optimal approach

def longest_subarray_with_sum_eq_k(arr,k):
    max_len = 0
    cur_sum = 0 
    freq = {0:-1}
    n = len(arr)
    for i in range(n):
        cur_sum += arr[i]
        
        past_sum = cur_sum - k
        
        if past_sum in freq:
            cur_len = i - freq[past_sum]
            max_len = max(max_len,cur_len)
            
        if cur_sum not in freq:
            freq[cur_sum] = i
            
    return max_len
print(longest_subarray_with_sum_eq_k([1,2,3,1,1,1],3))      #3