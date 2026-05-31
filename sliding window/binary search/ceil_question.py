
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
    ans = -1                    # if target is not found return - 1 
    while l <=r:
        mid = l+(r-l)//2
        if arr[mid] >= target:              # for the ceil question the formula is arr[mid] >= target that means the cur_mid_element is > = target then in generall what we will do if cur_ele is >= target we move the r = mid - 1 because to decrease to the target element
            ans = arr[mid]              # if target is found => return ans = arr[mid]  to override that ans = -1 if no target found simple return -1 
            r = mid - 1
        else:
            l = mid + 1
    return ans 
print(ceil_question([1,3,5,7],4))