from collections import deque

def count_at_most_k(arr, k):
    max_dq = deque()
    min_dq = deque()
    
    l = 0
    count = 0
    
    for r in range(len(arr)):
        
        while max_dq and arr[max_dq[-1]] < arr[r]:
            max_dq.pop()
        max_dq.append(r)
        
        while min_dq and arr[min_dq[-1]] > arr[r]:
            min_dq.pop()
        min_dq.append(r)
        
        while arr[max_dq[0]] - arr[min_dq[0]] > k:
            
            if max_dq[0] == l:
                max_dq.popleft()
            if min_dq[0] == l:
                min_dq.popleft()
                
            l += 1
        
        count += (r - l + 1)
    
    return count


def count_subarrays_ge_k(arr, k):
    n = len(arr)
    total = n * (n + 1) // 2
    
    return total - count_at_most_k(arr, k - 1)


print(count_subarrays_ge_k([1,3,2,5,4],2))

