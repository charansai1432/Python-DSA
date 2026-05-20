# Problem Statement

# Given sorted array with duplicates,
# return FIRST occurrence of target.

# If not found return -1.

# Example

# Input:

# arr = [1,2,2,2,3]
# target = 2

# Output:

# 1



# brute force approach

def first_occurance(arr,target):
    n  = len(arr)
    
    for num in arr:
        if num == target:
            return num
    return -1 
print(first_occurance([1,2,2,2,3],2))



# optimal solution approach 

def first_occurance(arr,target):
    l = 0 
    r = len(arr)-1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            ans = arr[mid]
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return ans 
print(first_occurance([1,2,2,2,3],2))