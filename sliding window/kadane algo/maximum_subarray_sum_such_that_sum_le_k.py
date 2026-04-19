
# This question in the optimal can be solved using the kadane's + prefix + binray search only we can solve this question 

# the optimal solution provides the TC=>O(n)

# the question we cannot using SW technique beacause if the array contains -ve elements we can't use the SW

# brute force approach 

def maximum_sum_subarray_sum_less_than_or_eq_k(arr,k):
    
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum <= k :
                max_sum = max(max_sum,cur_sum)
    return max_sum
print(maximum_sum_subarray_sum_less_than_or_eq_k([2,2,-1],3))


# optimal solution approach 

# formula ==> subarray sum = prefix[i] - prefix[j] (standard formula) for subarray sum AND slightly different from the 
# traditional formula in the prefix sum from this index to index i.e sum = prefix[j] - prefix[i-1]

# here for this subarray sum = prefix[j] - prefix[i]  

# i.e prefix[j]-prefix[i] <= k 

# we rearrange the terms then 

#prefix[i] >= prefix[j] - k  (>= used this condition for the solutino to be optimal as you know for the optimal solutino the condition should be greater than) (IN SIMPLE WORDS smallest prefix >= (cur_sum - k))
                                                 # past_sum = cur_sum - k
# HERE only prefix [j] = cur_sum 

# Why this works?

# Because:

# chosen prefix ≥ target
# ⇒ (prefix - chosen_prefix) ≤ k

# 👉 valid subarray

# Here the time complexity for this program is TC => O(n log n)

import bisect
def maximum_sum_subarray_sum_lessthan_eq_k(arr,k):
    max_sum = float('-inf')
    n = len(arr)
    cur_sum = 0
    sorted_arr = [0]
    
    for i in range(n):
        cur_sum += arr[i]
        
        target = cur_sum - k
        
        idx = bisect.bisect_left(sorted_arr,target)    # find the smallest prefix >= target
        
        if idx < len(sorted_arr):
            max_sum = max(max_sum,cur_sum - sorted_arr[idx])      # valid subarray sum <=k
            
        bisect.insort(sorted_arr,cur_sum)       # insert the cur_sum into the sorted_arr
        
    return max_sum 

print(maximum_sum_subarray_sum_lessthan_eq_k([2,2,-1],3))       #3


# Final Intuition (lock this)

# 👉
# At every step:

# compute prefix
# find best previous prefix using binary search
# update answer
# store current prefix


##################################################################################
# 🔥 Now your main doubt
# ❓ Why bisect_left, not bisect_right?

# This is VERY important.

# 🧠 First understand difference
# 🔹 bisect_left(arr, x)

# 👉 gives index of first element ≥ x

# 🔹 bisect_right(arr, x)

# 👉 gives index of first element > x

###################################################################################

# When to use which?
# ✅ Use bisect_left when:

# 👉 you need:

# first value ≥ target

# Used in:

# prefix sum ≤ k
# closest match problems
# ✅ Use bisect_right when:

# 👉 you need:

# first value > target

# Used in:

# strict comparisons
# upper bound cases
# 🎯 Simple rule (remember this)

# 👉
# “Need ≥ ? → use bisect_left”
# “Need > ? → use bisect_right”

# 🧠 Final intuition for THIS problem

# 👉 We want:

# prefix[i] ≥ target

# 👉 So:

# bisect_left(sorted_prefix, target)
# 👍 Quick check for you
# sorted_prefix = [1, 2, 4, 6]
# target = 4

# 👉 What will:

# bisect_left return?
# bisect_right return?

# Answer this — then this concept is fully solid 🚀