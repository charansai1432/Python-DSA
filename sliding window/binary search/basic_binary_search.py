

# Problem Statement

# Given a sorted array of integers and a target value,
# return the index of target.

# If target does not exist, return -1.

# Example

# Input:

# arr = [1,3,5,7,9]
# target = 7

# Output:

# 3
# Constraints
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9
# Array is sorted in ascending order

# brute force approach 

def basic_binary_search(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i 
    return -1
    
print(basic_binary_search([1,3,5,7,9],7))


# optimal solution approach


def basic_binary_search(arr,target):
    l = 0
    r = len(arr)-1
    
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
print(basic_binary_search([1,3,5,7,9],7))