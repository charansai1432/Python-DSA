
#brute force approach

def no_of_subarrays_sum_divisible_by_k(arr,k):
    count = 0
    # freq = {0:1}
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            
            if cur_sum %k == 0:
                count += 1
                
    return count
print(no_of_subarrays_sum_divisible_by_k([4,5,0,-2,-3,1],5))    #7


#optimal approach

def no_of_subarrays_sum_divisible_by_k(arr,k):
    count = 0
    n = len(arr)
    cur_sum = 0
    freq = {0:1}
    for i in range(n):
        
        cur_sum += arr[i]
        rem = cur_sum % k 
        
        if rem < 0:
            rem += k
        
        if rem in freq:
            count += freq[rem]
            
        freq[rem] = freq.get(rem,0)+1
    return count
print(no_of_subarrays_sum_divisible_by_k([4,5,0,-2,-3,1],5))    #7
        
        