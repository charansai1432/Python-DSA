
#Given an integer array and an integer k, find the maximum sum subarray with at most k elements.

# kadane algo question = > how ?? => max sum subbaray directly -> we have to use the kadane's for this question 
                                    # atmost k elements => this provides the condition 
                                    # That means we have in this variable size SW + kadane's algo approach we have to solve 


#imp => by default whenever we this question ==> brain goes to the varaibale SW with sum invalid condition but here they didnot given sum condtion ok 
# so this is a kadane algo question we took the size condition as invalid ==> imp


#brute force approah
def maximum_sum_subarray_atmost_k_elements(arr,k):
    
    max_sum = 0
    n = len(arr)
    for i in range(n):
        w_sum = 0
        for j in range(i,n):
            w_sum += arr[j]
            if (j-i+1) <= k:
                max_sum = max(max_sum,w_sum)
    return max_sum
print(maximum_sum_subarray_atmost_k_elements([2, -1, 3, -2, 4],3))  #5


# optimal approach

def max_sum_subarray_atmost_k_elements(arr,k):
    
    l = 0 
    max_sum = 0
    w_sum = 0
    for r in range(len(arr)):
        w_sum += arr[r]
        
        while (r-l+1) > k:
            w_sum -= arr[l]
            l+=1
            
        max_sum = max(max_sum,w_sum)
    return max_sum

  
print(max_sum_subarray_atmost_k_elements([2, -1, 3, -2, 4],3))

