# brute force approach 

def count_pairs_when_sum_lt_target(arr,target):
    
    count = 0
    
    for i in range(len(arr)):
        # cur_sum = 0
        for j in range(i+1,len(arr)):
                if arr[i] + arr[j] < target:
            
            
                    count += 1
    return count
print(count_pairs_when_sum_lt_target([1,2,3,4],6))      #4
    
    
# optimal solution 

def count_pairs_when_sum_lt_target(arr,target):
    n = len(arr)
    l  = 0
    r = n - 1
    count = 0
    while l < r:
        cur_sum = arr[l] + arr[r]
        if cur_sum < target:
            count += (r-l)
            l += 1
        else:
            r -= 1
    return count
        
print(count_pairs_when_sum_lt_target([1,2,3,4],6))      #4
        