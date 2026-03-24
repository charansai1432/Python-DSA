# brute force

def max_sum_subarray(arr,k):
    
    n = len(arr)
    max_sum = 0
    if n < k:
        return 

    for i in range(n - k + 1):
        win_sum = 0
        for j in range(i,i+k):
            win_sum += arr[j]
        max_sum = max(max_sum,win_sum)
    return max_sum
    
print(max_sum_subarray([2,1,5,1,3,2],3))   #9



#optimal solution 

def max_sum_subarray(arr,k):
    
    n = len(arr)
    
    if n < k:
        return 
    
    win_sum = sum(arr[:k])
    
    max_sum = win_sum

    for i in range(k,n):
        win_sum  = win_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum,win_sum)
    return max_sum
print(max_sum_subarray([2,1,5,1,3,2],3))  #9