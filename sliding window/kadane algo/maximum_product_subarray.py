#It is kadane's question because it has the (-ve) values,and question pattern seen to be like maximum sum subarray ==> maximum product subarray


#brute force approach 

def maxi_product_subarray(arr):
    max_prod = float('-inf')
    n = len(arr)
    for i in range(n):
        prod = 1
        for j in range(i,n):
            prod *= arr[j]            
            max_prod = max(max_prod,prod)
    return max_prod
print(maxi_product_subarray([2,3,-2,4]))

#optimal solution 

def maxi_product_subarray(arr):
    max_prod = min_prod = ans = arr[0]          # here are assuming the max and min element to be max,min,ans element
                                                # here at each step we track max and min product 
                                                # beacuse the array may also contain the -ve elements 
                                                # one of max_prod for postive values
                                                # one of min_prod for negative values
                                                
    for i in range(1,len(arr)):
        
        if arr[i] < 0:                                  # if the element has came the (-ve) element we have to swap because

                                                        # -ve * -ve element = postive element 
            max_prod,min_prod = min_prod,max_prod
            
        max_prod = max(arr[i] , arr[i]*max_prod)            # kadane's logic ==> max_product of (+ve) element gives postive elment
        min_prod = min(arr[i],arr[i]*min_prod)                  # -ve * -ve which gives big element 
        ans = max(ans,max_prod)
        
    return ans
print(maxi_product_subarray([2,3,-2,4]))
        
        
