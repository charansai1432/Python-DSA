
# brute force approach 

def min_value_in_rotated_sorted_array_II(arr):
    min_val = float('inf')
    n = len(arr)
    for i in range(n):
        min_val = min(min_val,arr[i])
    return min_val
print(min_value_in_rotated_sorted_array_II([1,2,3,3,4,5]))


# optimal solution approach 

def min_value_in_rotated_sorted_array_II(arr):
    l = 0
    r = len(arr) - 1
    min_val = float('inf')
    while l <= r:
        mid = l + (r-l)//2
        if arr[l] == arr[mid] == arr[r]:        # to handle the duplicates in the array if array having the duplicates and the l,r,mid having the same values then we cannot able to say the left half is sorted so we have to shirnk the array by the 'l' and 'r' pointer
            min_val = min(min_val,arr[l])       #{VVVVIMP}        # if a single element is there in the array then l = m = r at that time the min_val is same like either we can written the mid or l or r 
            l += 1
            r -= 1
        
        elif arr[l] <= arr[mid]:                # left half is sorted 
            min_val = min(min_val,arr[l])               # min_val always find in the arr[l] because array is sorted so left most element only having the min element
            l = mid + 1                             # here we dont do the r = mid -1 because min_val is already find right so we have to move forward (right side)
        
        
        else:                                                   # right half is sorted
            min_val = min(min_val,arr[mid])             # min_val is found in the mid only because in the rotated array the pivot element is where the array is rotated and that point (pivot) element only we have the min_val element
            r = mid -1                            # here we usually do the l = mid + 1 like to check the until the last element to find the min_value element
                                    #{VVVVIMP} array is sorted keep in brain example [3,4,5,0,1,2] that means min_val always find in the left side so (r = mid - 1)                    # but here min_val is always be in arr[mid] only and we go back side like (left side ) as array is sorted so min_val is always find in the left side so (r = mid - 1)
    return min_val
print(min_value_in_rotated_sorted_array_II([1,2,3,4,5]))
            
            
    