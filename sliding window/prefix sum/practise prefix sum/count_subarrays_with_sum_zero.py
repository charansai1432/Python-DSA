
#brute force approach

def count_subarrays_with_sum_zero(arr):
    count = 0
    n  = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            
            if cur_sum == 0:
                count += 1
    return count
print(count_subarrays_with_sum_zero([1,-1,0]))      #3


#optimal approach

def count_subarrays_with_sum_zero(arr):
    
    count = 0
    cur_sum = 0 
    n = len(arr)
    freq = {0:1}
    for i in range(n):
        cur_sum += arr[i]
        
        if cur_sum in freq:
            count += freq[cur_sum]
        freq[cur_sum] = freq.get(cur_sum,0)+1
    return count
print(count_subarrays_with_sum_zero([1,-1,0]))  #3