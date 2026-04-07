
#brute force approach

def length_of_largest_subarray_with_sum_eq_0(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum == 0:
                max_len = max(max_len,j-i+1)
    return max_len
print(length_of_largest_subarray_with_sum_eq_0([15,-2,2,-8,1,7,10,23]))     #5


#optimal solution 

def length_of_largest_subarray_with_sum_eq_0(arr):
    
    max_len = 0 
    cur_sum = 0
    n = len(arr)
    freq = {0:-1}
    for i in range(n):
        cur_sum += arr[i]
        
        if cur_sum in freq:
            cur_len = i - freq[cur_sum]
            max_len = max(max_len,cur_len)
        
        if cur_sum not in freq:
            freq[cur_sum] = i
    return max_len
print(length_of_largest_subarray_with_sum_eq_0([15,-2,2,-8,1,7,10,23])) #5