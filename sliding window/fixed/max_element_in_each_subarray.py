# brute force approach 

def max_element_in_each_subarray(arr,k):
    
    result = []
    n = len(arr)
    for i in range(n-k+1):
        max_ele = arr[i]
        
        for j in range(i,i+k):
            
            if arr[j] > max_ele:
                max_ele = arr[j]
                
        result.append(max_ele)
    return result
print(max_element_in_each_subarray([1,3,-1,-3,5,3,6,7],3))  #[3, 3, 5, 5, 6, 7]



#optimal solution using the deque

from collections import deque

def max_element_in_each_subarray(arr,k):
    
    n = len(arr)
    
    dq = deque()
    result = []
    
    for i in range(n):
        window_start  = i - k + 1
        
        if dq and dq[0] < window_start:
            dq.popleft()
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

print(max_element_in_each_subarray([1,3,-1,-3,5,3,6,7],3))  #[3, 3, 5, 5, 6, 7]