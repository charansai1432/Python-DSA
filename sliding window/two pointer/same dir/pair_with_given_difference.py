
# Problem: Pair With Given Difference
# 🧾 Interview-style Question

# “Given an array and a target difference k, check whether there exists a pair (a, b) such that:

# b - a = k

# Return True if such pair exists, otherwise False.

# 🔍 Example 1
# Input:
# arr = [1, 5, 3, 4, 2]
# k = 2

# Output:
# True
# ✅ Why?

# Because:

# 3 - 1 = 2
# 5 - 3 = 2
# 4 - 2 = 2
# 🔍 Example 2
# Input:
# arr = [10, 20, 30]
# k = 15

# Output:
# False
# 🧠 How to IDENTIFY this pattern

# Ask yourself:

# Pair problem? ✅
# Difference comparison? ✅
# Can sorting help? ✅
# Need better than O(n²)? ✅

# 👉 Think:

# Sort + Two Pointers


###### This problem is a classic two pointer -> same direction problem #########


# brute force approach 

def pair_with_given_difference(arr,k):
    arr.sort()
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1,n):
            diff = abs(arr[j] - arr[i])
            if diff == k:
                return True
    return False
print(pair_with_given_difference([1, 5, 3, 4, 2],2))


# optimal solution can be done with the help of same direction two pointer technique

def pair_with_given_difference(arr,k):
    n = len(arr)
    l = 0 
    r = 1 
    while r < n:
        
        diff = abs(arr[r] - arr[l])
        
        if diff < k:
            r += 1
        elif diff > k:
            l += 1
        elif l == r:
            r += 1
        elif diff  == k:
            return True
    return False
# print(pair_with_given_difference([1, 5, 3, 4, 2],2))
print(pair_with_given_difference([10, 20, 30],15))