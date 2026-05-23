

# brute force approach 

def single_element_in_sorted_array(arr):
    from collections import Counter
    freq = Counter(arr)
    for num in arr:
        if freq[num] == 1:
            return num 
#     return -1
# print(single_element_in_sorted_array([1,1,2,2,3,3,4]))
# print(single_element_in_sorted_array([1,1,2,2,3,3]))
# print(single_element_in_sorted_array([0,0,0,0]))
# print(single_element_in_sorted_array([]))


# optimal solution approach 


def single_element_in_sorted_array(arr):
    n = len(arr)
    l = 0
    r = n - 1 
    if len(arr) == 0:
        return -1 
    while l < r:
        mid = l + (r - l )//2
        if mid % 2 == 1:
            mid -= 1
        if arr[mid] == arr[mid+1]:
            l = mid + 2
        elif arr[mid] != arr[mid+1]:
            r = mid
            
    return arr[r]
print(single_element_in_sorted_array([1,1,2,2,3,3,4]))
print(single_element_in_sorted_array([1,1,2,2,3,3]))
print(single_element_in_sorted_array([0,0,0,0]))
print(single_element_in_sorted_array([]))
