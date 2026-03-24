#optimal solution 

def count_no_of_subarrays_atmost_equal_k(arr,k):
    
    from collections import deque
    
    max_dq = deque()
    min_dq =deque()
    
    count = 0
    
    l = 0
    
    for r in range(len(arr)):
        
        while max_dq and arr[max_dq[-1]] < arr[r]:
            max_dq.pop()
            
        while min_dq and arr[min_dq[-1]] > arr[r]:
            min_dq.pop()
            
        max_dq.append(r)
        min_dq.append(r)
        
        while (arr[max_dq[0]] - arr[min_dq[0]]) > k:
            
            if max_dq[0] == l :
                max_dq.popleft()
            
            if min_dq[0] == l :
                min_dq.popleft()
            
            l += 1
            
        count += (r-l+1)
    return count


def count_subarray_exactly_equal_k(arr,k):
    return count_no_of_subarrays_atmost_equal_k(arr,k) - count_no_of_subarrays_atmost_equal_k(arr,k-1)

print(count_subarray_exactly_equal_k([1,3,2,5,4],2))