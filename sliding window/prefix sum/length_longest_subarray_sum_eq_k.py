# Problem (new)
# arr = [1, 2, 3, 1, 1, 1]
# k = 3

# 👉 Question:
# Find the length of the longest subarray whose sum = k

## here it is a prefix sum question == how ?? ==> if a question says directly sum = k prefix sum == > and constraint values tells array 
# array can contain -ve values then the pattern become kadane's algo or prefix sum 


# here it is just a prefix sum ==> why ?? ==> all the PREFIX SUM patterns which include the sum = k (OR) sum divisable by k (OR) prefix sum array 
# this is such cases we use only prefix sum approach okk

#kadane algo in the question mostly we can able to see the max sum subarray in that case we have to use the kadane algo
# in prefix sum we actually have the range from this index to index and count subarray sum == k , longest subarray == k in this case we use the prefix sum 

#Here generally for every prefix sum problem in the opimal approach we use the for loop and cur_sum like count subarry,longest subarray question we calculate the cur_sum okk

# but for the prefix sum array with the mentioned ranges we use this formula like prefix[i] = arr[i] + prefix[i-1]

# now the question is 

def length_longest_subarray_sum_eq_k(arr,k):
    cur_sum = 0
    max_len = 0
    freq = {0:-1}
    for i in range(len(arr)):
        cur_sum += arr[i]
        past_sum = cur_sum - k
        
        if past_sum in freq:
            cur_len= i- freq[past_sum]
            max_len = max(max_len,cur_len)

        if cur_sum not in freq:     # here this condition we definately has to be returned in the question like not in count problems ,length subarray questions because here we are finding the earliest possible subarray count or longest subarray(sum) == k 
            freq[cur_sum] = i           # here we are not storing the sum frequnecy here are just storing the index of the cur_sum
            
    return max_len
# print(length_longest_subarray_sum_eq_k([1, 2, 3, 1, 1, 1],3)) #3

print(length_longest_subarray_sum_eq_k([2,1,1,1],2))


