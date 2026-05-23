
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
        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
# print(search_in_rotated_sorted_array([3,4,5,6,0,1,2],0))      #4
# print(search_in_rotated_sorted_array([],0))
print(search_in_rotated_sorted_array([3,3,3,4,4,5],5))