
# ✅ Case 2: Circular subarray (wrapping)

# 👉 Trick:

# circular_sum = total_sum - minimum_subarray_sum


# Why this works?

# Instead of finding what to take…

# 👉 we find what to remove

####################################################################################################

# brute force approach 

# It is circular subarray so we have to add the array to itself

def maximum_sum_circular_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    extend_arr = arr + arr
    for i in range(n):
        cur_sum = 0
        for j in range(i,i+n):              # here the i+n is used because we aren't stopping at last element we are continuing to the first element again 
            
            cur_sum += extend_arr[j]
            max_sum = max(max_sum,cur_sum)
    return max_sum
print(maximum_sum_circular_subarray([5,-3,5]))      #10 
    
    
    
# optimal solution approach 

def maximum_sum_circular_subarray(arr):
    n = len(arr)
    max_sum = cur_max_sum = arr[0]                        # here for the both max_sum and cur_max_sum = arr[0] beacuse here the subarray should non empty 
    min_sum = cur_min_sum =  arr[0]                                # if the subarray can be empty then we can take the min and max_sum to be 0 or float('-inf)
    
    for i in range(1,len(arr)):
        cur_max_sum = max(arr[i] , arr[i] + cur_max_sum )       # here we are caculating the max_sum for traditional max_sum 
        max_sum = max(max_sum,cur_max_sum)  
    # print(max_sum)                                          ## for the circular max_sum question we have to calculate the both max_sum and total - min_sum_subarray right 
        
    for i in range(1,len(arr)):
        cur_min_sum = min(arr[i],arr[i]+cur_min_sum)
        min_sum = min(min_sum,cur_min_sum)
    # print(min_sum)
        
    circular_sum = sum(arr) - min_sum                               #
    # print(circular_sum)                                                           # circular_sum = total_sum - minimum_subarray_sum
                                                                # this only gives the circular sum not max_sum 
    if max_sum < 0:         # edge case handling if max_sum < 0 
        return max_sum                  # that means in the case of all elements in the arrays is (-ve) then max_sum < 0 right 
    
    return max(max_sum,circular_sum)

print(maximum_sum_circular_subarray([5,-3,5])) #10


# print(maximum_sum_circular_subarray([3, -1, 2, -1]))        #4