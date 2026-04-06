#optimal approach
def count_subarrays_whose_sum_is_divisible_by_k(arr,k):
    
    count = 0
    n = len(arr)
    cur_sum = 0
    
    freq = {0:1}
    for i in range(n):
        cur_sum += arr[i]
        
        rem =  cur_sum%k
        
        if rem < 0:
            rem += k
        
        if rem in freq:
            count += freq[rem]
        
        # if rem not in freq:
        freq[rem] = freq.get(rem,0)+1
    return count

print(count_subarrays_whose_sum_is_divisible_by_k([4, 5, 0, -2, -3, 1],5))          #7