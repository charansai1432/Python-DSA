
# # brute force approach

# def three_sum(arr,target):
#     n = len(arr)
#     result = []
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if arr[i] + arr[j] + arr[k] == target:
#                     result.append([arr[i],arr[j],arr[k]])

#     return result
# print(three_sum( [-1, 0, 1, 2, -1, -4],0))

# optimal solution approach

def three_sum(arr):
    n = len(arr)
    arr.sort()
    result = []
    for i in range(n):
        
        if i > 0 and arr[i] == arr[i-1]:     #“If current element is SAME as previous one, skip it”    ## Avoid starting same triplet    ##  Avoid repeating same triplet  ## “Don’t start with the same number twice”
            continue
        
        left = i+1
        right = n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:                                                              # Why move both pointers after finding a triplet? Because that pair has already been used, 
                                                                                                # and moving both pointers ensures we explore new combinations while avoiding duplicate results.
                result.append([arr[i],arr[left],arr[right]])
                left+= 1
                right -= 1
                
                while left < right and arr[left] == arr[left-1]:                #Skip all duplicate 0s  ## Avoid repeating same pair
                    left+=1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
print(three_sum([-1, 0, 1, 2, -1, -4]))
            
            