
# brute force approach 


def ceil_question(arr,target):
    n = len(arr)
    ans = -1 
    for num in arr:
        if num >= target:
            ans = num 
            break
    return ans
        
print(ceil_question([1,3,5,7],4))


# optimal solution approach 

def ceil_question(arr,target):
    l = 0 
    r = len(arr)-1
    ans = -1
    while l <=r:
        mid = l+(r-l)//2
        if arr[mid] >= target:
            ans = arr[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans 
print(ceil_question([1,3,5,7],4))