#brute force approach

def count_subarrays_with_given_XOR_eq_k(arr,k):
    count = 0
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum ^= arr[j]
            
            if cur_sum == k:
                count += 1
    return count
print(count_subarrays_with_given_XOR_eq_k([4,2,2,6,4],6))       #4


#optimal solution 

def count_subarrays_with_given_XOR_eq_k(arr,k):
    count = 0
    cur_sum = 0 
    n = len(arr)
    freq = {0:1}
    for i in range(n):
        cur_sum ^= arr[i]
        
        past_sum = cur_sum ^ k
        
        if past_sum in freq:
            count += freq[past_sum]
            
        freq[cur_sum] = freq.get(cur_sum,0)+1
    return count
print(count_subarrays_with_given_XOR_eq_k([4,2,2,6,4],6))   #4