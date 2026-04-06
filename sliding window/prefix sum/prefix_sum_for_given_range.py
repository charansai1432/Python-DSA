#optimal approach
def prefix_sum_for_given_range(arr):
    
    p_sum = arr[0]
    p_sum = [0] * len(arr)
    n  = len(arr)
    
    for i in range(1,n):
        p_sum[i] = arr[i] + p_sum[i-1]
        
    i,j = 1,3           # from this position to pos use the below formula
    
    if i == 0:
        return p_sum[j]
    
    return (p_sum[j]-p_sum[i-1])        #sum(3->10) = (i-j) = p_sum[j] - p_sum[i-1]

print(prefix_sum_for_given_range([1,2,3,4]))