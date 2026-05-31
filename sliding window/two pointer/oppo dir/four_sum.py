

# this is a question where we have to find a 4 elements sum is equal to 0 this is the main motive of the 4sum and also it the qudralet doesnot contain any duplicate 


#brute force approach 

def four_sum(arr,total):
    n = len(arr)
    result = []
    arr.sort()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[k] == total:
                        result.append([arr[i],arr[j],arr[k],arr[l]])
    return result
print(four_sum([1,2,3,4,5,0,0,0],0))



# The optimal approach could be the fix two values and then apply the two pointer technique { 2 values fix + two pointer }approach 
# optimal solution approach

def four_sum(arr,target):
    n  = len(arr)
    result = []
    arr.sort()
    for i in range(n-3):                        # n - 3 which the how many times it has to iterate 
        
        if i > 0 and arr[i] == arr[i-1]:            # for checking the duplicates 
            continue                        # stop the iteration and continue with the next iteration 
        
        for j in range(i+1,n-2):                 # for fixing the 2nd value in an array 
            if j > i+1 and arr[j] == arr[j-1]:  
                continue
            
            l = j + 1                               # actual 2-pointer technique
            r = n - 1
            
            while l < r:
                total = arr[i] + arr[j] + arr[l] + arr[r]
                
                if total == target:
                    result.append([arr[i],arr[j],arr[l],arr[r]])
                    l+=1                                    # l += 1 to check whether next value can form a value = 0
                    r-=1                                       # on both sides we to shrink to check for the next unique qudralet
                    
                while l < r and arr[l] == arr[l-1]:       # checking the duplicates from the left side 
                    l += 1
                while l < r and arr[r] == arr[r + 1]:       # checking the duplicates from the right side
                    r -= 1
                    
                if total < target:          # traditional appraoch 
                    l += 1
                else:
                    r -= 1
    return result

print(four_sum([1,2,3,4,5,5,6,6],6))
        