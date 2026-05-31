
# Problem Statement

# Return first index where:

# arr[i]>target
# Example

# Input:

# arr = [1,2,2,2,5]
# target = 2

# Output:

# 4

#  for the lower bound ==> arr[mid] >= target ==> lower bound 
# for the upper bound  ==> arr[mid] > target  ==> upper bound 

# brute force approach

def upper_bound(arr,target):
    n = len(arr)
    
    for i in range(n):
        if arr[i] > target:
            ans = i
    return ans
print(upper_bound([1,2,2,2,5],2))


# optimal solution approach 


def upper_bound(arr,target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] > target:
            ans = mid
            r = mid -1
        else:
            l = mid +1
    return ans
print(upper_bound([1,2,2,2,5],2))
