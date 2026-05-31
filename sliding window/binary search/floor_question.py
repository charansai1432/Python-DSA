
#For the floor question the condition could be the <= 

# and for the ceil question the condition could be the >= 

# for the floor question the formula is arr[mid] <= target that means the cur_mid_element is <= target then in generall what we will do if cur_ele is <= target we move the  l = mid + 1 because to increase  to the target element
                         # if target is found => return ans = arr[mid]  to override that ans = -1 if no target found simple return -1 
            

# brute force approach 

def floor_question(arr,target):
    n = len(arr)
    ans = -1
    for i in range(n):
        if arr[i] <= target:
            ans = arr[i]
    return ans
print(floor_question([1,3,5,7],4))


# optimal solution approach 

def floor_question(arr,target):
    n = len(arr)
    l = 0
    r = n - 1
    ans = -1 
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] <= target:
            
            ans = arr[mid]
            l = mid + 1
        else:
            r = mid - 1
    return ans
print(floor_question([1,3,5,7],4))

    