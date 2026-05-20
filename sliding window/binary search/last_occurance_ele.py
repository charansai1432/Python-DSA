
# Problem Statement

# Return LAST occurrence of target.

# Example

# Input:

# arr = [1,2,2,2,3]
# target = 2

# Output:

# 3


# brute force approach 

def last_occurance(arr,target):
    n = len(arr)
    for i in range(n-1,-1,-1):
        if arr[i] == target:
            return i 
    return -1 
print(last_occurance([1,2,2,2,3],2))


# optimal solution approach

def last_occurance(arr,target):
    l = 0 
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            ans = mid 
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return ans
print(last_occurance([1,2,2,2,3],2))