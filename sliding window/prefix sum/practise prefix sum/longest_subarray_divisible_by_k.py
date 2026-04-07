
#brute force approach

def longest_subarray_divisible_by_k(arr,k):
    max_len = 0
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            
            if cur_sum % k  == 0:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_subarray_divisible_by_k([2,7,6,1,4,5],3))     #4

#optimal solution 

def longest_subarray_divisible_by_k(arr,k):
    max_len = 0
    n = len(arr)
    freq = {0:-1}
    cur_sum = 0
    for i in range(n):
        cur_sum += arr[i]
        
        rem = cur_sum % k
        
        if rem < 0:
            rem += k
            
        if rem in freq:
            cur_len = i - freq[rem]
            max_len = max(max_len,cur_len)
        
        if rem not in freq:
            freq[rem] = i
    return max_len
print(longest_subarray_divisible_by_k([2,7,6,1,4,5],3)) #4