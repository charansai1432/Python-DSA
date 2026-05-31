# Problem Statement

# Return first index where:

# arr[i]≥target

# If no such index exists,
# return len(arr).

# Example

# Input:

# arr = [1,3,3,5,8]
# target = 4

# Output:

# 3

# Because:
# 5 is first element ≥ 4.

#  for the lower bound ==> arr[mid] >= target ==> lower bound 
# for the upper bound  ==> arr[mid] > target  ==> upper bound 

# brute force approach 

def lower_bound(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] >= target:
            return i
    return len(arr)
print(lower_bound([1,3,3,5,8],4))


# optimal solution approach

def lower_bound(arr,target):
    n = len(arr)
    l = 0
    r = n - 1
    ans = n
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] >= target:
            ans = mid
            r  = mid - 1
        else:
            l= mid + 1
    return  ans
print(lower_bound([1,3,3,5,8],4))


