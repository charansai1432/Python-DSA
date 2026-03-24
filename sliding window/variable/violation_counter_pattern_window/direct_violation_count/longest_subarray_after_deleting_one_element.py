#brute force

def longest_subarray_after_deleting_one_element(arr):
    max_len = 0
    n = len(arr)
    
    for i in range(n):
        zero_count = 0
        for j in range(i,n):
            if arr[j] == 0:
                zero_count += 1
                
            if zero_count == 1:
                max_len = max(max_len,j-i)
    return max_len
print(longest_subarray_after_deleting_one_element([1,1,0,1,1,1,0,1]))   #5


#optimal solution 
def longest_subarray_after_deleting_one_element(arr):
    
    l = 0 
    max_len = 0
    zero_count = 0
    
    for r in range(len(arr)):
        if arr[r] == 0:
            zero_count += 1
        while zero_count > 1:
            
            if arr[l] == 0:
                zero_count -= 1
                
            l +=1
        max_len = max(max_len,r-l)   # Here in this question we are using the r - l only 
                                    # beacuse r - l + 1 which gives the entire window length i.e [1,2,3,4,5] -> len = 5(r-l+1) ==> here in the question after shrinking we remove one element from the window that's why r -l is used in general (r-l+1) -1 => r - l here  -1 is removing one element asked in the question 
    return max_len

print(longest_subarray_after_deleting_one_element([1,1,0,1,1,1,0,1])) #5
            