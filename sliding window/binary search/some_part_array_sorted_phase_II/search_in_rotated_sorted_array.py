# return the target index in a array other wise -1 return 
# brute force approach 

def search_in_rotated_sorted_array(arr,target):
    
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i 
    return -1 
# print(search_in_rotated_sorted_array([3,4,5,6,0,1,2],0))  #4


# optimal solution approach

def search_in_rotated_sorted_array(arr,target):
    n = len(arr)
    l = 0
    r = n -1 
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        if arr[l] <= arr[mid]:                  # left half is sorted 
            if arr[l] <= target <= arr[mid]:            # in the left half is my target is present or not check if yes ? => then move the right pointer towards left side 
                r = mid - 1
            else:                                   # if target isn't found at the left side move the 'l' pointer towards right side
                l = mid + 1
                
        else:                                           # condition for the right half is sorted and then search for the target in the right half sorted side by moving the left pointer towards right side 
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:                                       # if target is not found at sorted right side try to move the r pointer towards the left side even though the target is not found then return -1 
                r = mid - 1
    return -1
# print(search_in_rotated_sorted_array([3,4,5,6,0,1,2],0))      #4
# print(search_in_rotated_sorted_array([],0))
print(search_in_rotated_sorted_array([3,3,3,4,4,5],5))