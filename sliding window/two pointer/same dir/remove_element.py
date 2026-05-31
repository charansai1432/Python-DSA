
# brute force approach 

def remove_element(arr,val):
    uniq = []
    for num in arr:
        if num != val:
            uniq.append(num)
    return len(uniq)
    
print(remove_element([3,2,2,3],3))


# optimal solution approach 

def remove_element(arr,val):            # remove_element == > we have to keep elements other than that value 
    n = len(arr)
    slow = 0
    for fast in range(n):
        if arr[fast] != val:                # this condition gives the elements other than that value
            arr[slow] = arr[fast]
            slow +=1
    return  slow 
print(remove_element([3,2,2,3],3))