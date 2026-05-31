#  here we have to find the minimum value in a rotated sorted array 
#  for the minimum_val we have to choose a value from a large side 

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
            min_val = min(min_val,arr[l])            # if the entire array is sorted the min_val is always lies at left starting point
            
            break
        
        elif arr[l] <= arr[mid]:                        # this condition which gives the left side is sorted 
            min_val = min(min_val,arr[l])                   # if the left half is sorted the min_val lies in the left most element (beacuse array is sorted)
            l = mid + 1                                 # we move the left pointer forward even though min_val is find above===> why ? 
                                                        # because we find the min_val in the left side only not on the entire array example:- [3,4,5,1,2] at this time the min_val for entire rotated sorted is array is '1'
                                                                
        elif arr[mid] <= arr[r]:                        # right half is sorted
            min_val = min(min_val,arr[mid])                     # the right half is sorted the min_val lies in the mid position 
            r = mid - 1                                 # r = mid -1 which performs the r pointer to move left side to find the min_val in right sorted half for example:- [3,4,5,1,2] at this time 'l' pointer moves right and 'r' pointer moves left as array is sorted the min_val must be find in the left side then (r = mid - 1)
    return min_val
print(min_value_in_rotated_sorted_array([0,1,2,3,4,4,5]))
print(min_value_in_rotated_sorted_array([0,0,0,0,0]))
print(min_value_in_rotated_sorted_array([]))
        