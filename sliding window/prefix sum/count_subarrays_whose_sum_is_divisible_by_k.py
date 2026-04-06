#optimal approach
def count_subarrays_whose_sum_is_divisible_by_k(arr,k):
    
    count = 0
    n = len(arr)
    cur_sum = 0
    
    freq = {0:1}
    for i in range(n):
        cur_sum += arr[i]
        
        rem =  cur_sum%k
        
        if rem < 0:             #To handle the negative values i.e the remainder can also be negative in such case this condition is used 
            rem += k
        
        if rem in freq:
            count += freq[rem]
        
        # if rem not in freq:
        freq[rem] = freq.get(rem,0)+1
    return count

print(count_subarrays_whose_sum_is_divisible_by_k([4, 5, 0, -2, -3, 1],5))          #7



# What does rem += k do?

# If:

# rem = -2
# k = 5

# Then:

# rem += k  →  -2 + 5 = 3

# 👉 It converts a negative remainder into correct positive remainder

# 🔥 Why is this necessary?

# Because we use rem as a key in hashmap

# If you don’t fix it:

# One time remainder = 3
# Another time remainder = -2

# 👉 These should be treated as SAME (mathematically)
# 👉 But hashmap treats them as DIFFERENT ❌