# brute force

def first_negative_element(arr,k):
    
    n = len(arr)
    result = []
    for i in range(n-k+1):
        found = False
        for j in range(i,i+k):
            if arr[j] < 0:
                result.append(arr[j])
                found = True
                break
        else:
            result.append(0)
    return result
    
    
print(first_negative_element([12,-1,-7,8,-15,30,16,28],3)) #[-1, -1, -7, -15, -15, 0]


# optimal solution -> using dequqe

from collections import deque

def first_negative_element(arr,k):
    
    n = len(arr)
    
    dq = deque()
    
    result = []
    for i in range(n):
        
        window_start = i - k+1
        
        
        if dq and dq[0] < window_start:
            dq.popleft()
         
        if arr[i] < 0 :
            dq.append(i)
            
        if i >= k -1:
            if dq:
                result.append(arr[dq[0]])
            else:
                result.append(0)
    return result
print(first_negative_element([12,-1,-7,8,-15,30,16,28],3))  #[-1, -1, -7, -15, -15, 0]