
# brute force approach
def search_in_rotated_sorted_array_II(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i,arr[i]
    return -1 
# print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],5))
# print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],6))


# optimal solution approach 

def search_in_rotated_sorted_array_II(arr,target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid 
        if arr[l] == arr[r] == arr[mid]:
            l += 1
            r -= 1
            
        elif arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                
                r = mid - 1
            else:
                l = mid + 1
        elif arr[mid] <= arr[r]:
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1 

# print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],5))
print(search_in_rotated_sorted_array_II([3,4,5,0,1,2],6))
            
