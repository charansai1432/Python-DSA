
# brute force approach
def search_in_rotated_sorted_array_II(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i,arr[i]
    return -1 
# print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],5))
# print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],6))


# optimal solution approach 

def search_in_rotated_sorted_array_II(arr,target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid 
        if arr[l] == arr[r] == arr[mid]:            # to handle duplicates in the array 
            l += 1
            r -= 1
            
        elif arr[l] <= arr[mid]:        # left half is sorted 
            if arr[l] <= target <= arr[mid]:        # to search for the target in the left side we have to move towards left side (r = mid - 1)
                
                r = mid - 1
            else:                       # if target is not found in the left half sorted array move the left pointer towards (right side)
                l = mid + 1                     # so l = mid +1 
        
        elif arr[mid] <= arr[r]:                # if right half is sorted 
            if arr[mid] <= target <= arr[r]:            # to search the target in the right sorted half to seearch for the right side move the left pointer towards the (right side)
                l = mid + 1                                 # so l = mid + 1
            
            else:                                               # if right half is not sorted move the 'r' pointer towards left side 
                r = mid - 1                          # so r = mid - 1 
    return -1                                                   # if no target found return '-1'

# print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],5))
print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],6))
            
