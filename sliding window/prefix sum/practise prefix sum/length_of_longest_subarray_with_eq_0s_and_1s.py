
#brute force approach
def length_of_longest_subarray_with_eq_0s_and_1s(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        zero_count = 0
        one_count = 0
        for j in range(i,n):
            if arr[j] == 0:
                zero_count += 1
                
            else:
                one_count += 1
                
            if zero_count ==  one_count:
                max_len = max(max_len,j-i+1)
    return max_len
print(length_of_longest_subarray_with_eq_0s_and_1s([0,1,0,1,1,0]))      #6


#optimal approach

def length_of_longest_subarray_with_eq_0s_and_1s(arr):
    max_len = 0
    freq = {0:-1}
    cur_sum = 0 
    
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            cur_sum += -1
        else:
            cur_sum += 1
            
        if cur_sum in freq:
            cur_len = i - freq[cur_sum]
            max_len = max(max_len,cur_len)
        
        if cur_sum  not in freq:
            freq[cur_sum] = i
    return max_len
print(length_of_longest_subarray_with_eq_0s_and_1s([0,1,0,1,1,0]))      #6