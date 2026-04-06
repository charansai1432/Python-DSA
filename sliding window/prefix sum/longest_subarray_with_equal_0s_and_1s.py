
# arr = [0, 1, 0, 1, 1, 0]

# 👉 Question:
# Find the longest subarray with equal number of 0s and 1s

# 🧠 First: Why normal thinking fails?

# You might think:

# count 0s
# count 1s

# But for every subarray → too slow ❌

# 🔥 Trick (VERY IMPORTANT)

# 👉 Convert:

# 0 → -1
# 1 → 1
# 🧠 Why this works (simple logic)

# If:

# equal 0s and 1s

# After conversion:

# sum = 0
# 🔍 Example
# [0,1] → [-1,1] → sum = 0 ✅
# [0,1,0,1] → [-1,1,-1,1] → sum = 0 ✅
# 🎯 So problem becomes:

# 👉
# Find longest subarray with sum = 0



#### above is the question and how to approach it above it also tells why the native approach doesnot suite because it's slow


#brute force approach 

def longest_subarray_with_equal_0s_and_1s(arr):
    n = len(arr)
    freq = {0:-1}
    max_len = 0
    for i in range(n):
        cur_sum =0 
        for j in range(i,n):
            if arr[j] == 0:
                cur_sum += -1
            else:
                cur_sum += 1
                
            if cur_sum in freq:
                cur_len = j - freq[cur_sum]
                max_len = max(max_len,cur_len)
            
            if cur_sum not in freq:
                freq[cur_sum] = i
    return max_len
print(longest_subarray_with_equal_0s_and_1s([0, 1, 0, 1, 1, 0]))    #6



#optimal approach
def longest_subarray_with_equal_0s_and_1s(arr):
    
    freq = {0:-1}
    cur_sum = 0
    n = len(arr)
    max_len = 0
    for i in range(n):
        if arr[i] == 0:
            cur_sum += -1
        else:
            cur_sum += 1                
                                        # here k = 0 in question they didn't but we know how?? if we make 0's -> -1 and 1's -> 1 
                                        # Then -1 + 1 = 0 i.e sum = 0 ok then k = 0 (logic)     (IMPORTANT)
        # past_sum = cur_sum - k          # here  k =  0 i,e past_sum = cur_Sum - 0 ===> past_sum = cur_sum
        
        if cur_sum in freq:
            cur_len = i - freq[cur_sum]
            max_len = max(max_len,cur_len)
            
        if cur_sum not in freq:
            freq[cur_sum] = i
    return max_len
print(longest_subarray_with_equal_0s_and_1s([0, 1, 0, 1, 1, 0]))        #6