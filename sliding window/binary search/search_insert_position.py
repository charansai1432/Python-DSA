
# Problem Statement

# If target exists,
# return index.

# Otherwise return position where it should be inserted.

# Example

# Input:

# arr = [1,3,5,6]
# target = 2

# Output:

# 1

# Because 2 should be inserted at index 1.



# brute force approach 

import bisect
def search_insert_positon(arr,target):
    
    pass
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i 
    idx = bisect.bisect_left(arr,target)
    return idx
print(search_insert_positon([1,3,5,6],2))

# optimal solution approach 

def search_insert_position(arr,target):
    n = len(arr)
    l = 0 
    r = n - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans
print(search_insert_position([1,3,5,6],2))



# optimal solution using some more inbuilt technique

def search_insert_position(arr,target):
    l = 0 
    r = len(arr) - 1
    n  = len(arr)
    import bisect
    for i in range(n):
        if arr[i] == target:
            return i 
    idx = bisect.bisect_left(arr,target)
    return idx
print(search_insert_position([1,3,5,6],2))

    