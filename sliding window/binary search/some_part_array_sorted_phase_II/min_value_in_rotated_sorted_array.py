# brute force approach 

def min_value_in_rotated_sorted_array(arr):
    n = len(arr)
    min_val = float('inf')
    for i in range(n):
        min_val = min(min_val,arr[i])
    return min_val
# print(min_value_in_rotated_sorted_array([1,2,3,4,4,5]))


# optimal solution approach 

def min_value_in_rotated_sorted_array(arr):
    n = len(arr)
    min_val = float('inf')
    l = 0
    r = n - 1
    while l <= r:
        mid = l + (r-l)//2
        
        if arr[l] <= arr[r]:
            min_val = min(min_val,arr[l])
            
            break
        elif arr[l] <= arr[mid]:
            min_val = min(min_val,arr[l])
            l = mid + 1
        
        elif arr[mid] <= arr[r]:
            min_val = min(min_val,arr[mid])
            r = mid - 1
    return min_val
print(min_value_in_rotated_sorted_array([0,1,2,3,4,4,5]))
print(min_value_in_rotated_sorted_array([0,0,0,0,0]))
print(min_value_in_rotated_sorted_array([]))
        