#brute force approach

def count_subarrays_with_eq_0s_and_1s(arr):
    count = 0
    for i in range(len(arr)):
        zero_count = 0
        one_count = 0
        for j in range(i,len(arr)):
            if arr[j] == 0:
                zero_count += 1
            else:
                one_count += 1
            if zero_count == one_count:
                count += 1
    return count
print(count_subarrays_with_eq_0s_and_1s([0,1,0]))       #2
    
#optimal approach

def count_subarrays_with_eq_0s_and_1s(arr):
    count = 0
    freq = {0:1}
    cur_sum =0 
    n = len(arr)
    
    for i in range(n):
        cur_sum += arr[i]
        
        if cur_sum in freq:
            count += freq[cur_sum]
        
        freq[cur_sum] = freq.get(cur_sum,0)+1
    return count
print(count_subarrays_with_eq_0s_and_1s([0,1,0]))       #2