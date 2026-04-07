
#brute force approach

def total_number_of_subarrays_sum_eq_k(arr,k):
    count = 0
    freq = {0:1}
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            
            past_sum = cur_sum - k
            
            if past_sum in freq:
                count += freq[past_sum]
        freq[cur_sum] = freq.get(cur_sum,0)+1
    return count
print(total_number_of_subarrays_sum_eq_k([1,2,3],3))        #2



#optimal approach

def total_number_of_subarrays_with_sum_eq_k(arr,k):
    count = 0
    cur_sum = 0
    freq = {0:1}
    n = len(arr)
    for i in range(n):
        cur_sum += arr[i]
        
        past_sum = cur_sum - k
        
        if past_sum  in freq:
            count += freq[past_sum]
            
        freq[cur_sum] = freq.get(cur_sum,0)+1
    return count
print(total_number_of_subarrays_with_sum_eq_k([1,2,3],3))       #2
    