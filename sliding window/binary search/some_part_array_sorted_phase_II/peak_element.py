
# peak element is a question the element should have the neighbouring element is small then it is a peak element
# the neighbouring element should be small compared to the cur_element
#  for example [1,1,2,3,5,4,4] ===> the peak element is '5'.

# Here the array may or may not be sorted also then we can perform the binary search 

# brute force approach

def peak_element(arr):
    n = len(arr)

    for i in range(n):
                                                            # here i = 0 that we are the 1st index position that we have the right value to compare for peak element but we dont have the left value so for the left value we choose the left = float('-inf') {only at index = 0 postion float=('inf') } and if the index is at '3' then the left element should be the cur_index -1 which gives the left side element to the cur_element
        left = float('-inf') if i == 0 else arr[i-1]            # in this brute force approach we took the float('-inf') because we want a postive value so we compared from the big negative value
        right = float('-inf') if i == n-1 else arr[i+1]     # here at last index right is float=('-inf') => i = n - 1 that means it is last index,, here if the index is at '2' the left element is given by the above one and right element should be given by the i = i + 1 i.e next element to cur_element ==. i + 1

        if arr[i] > left and arr[i] > right:
            return i
        
print(peak_element([1,2,3,1]))

# optimal solution approach

def peak_element(arr):
    n = len(arr)
    l = 0
    r = n  -1
    while l < r:
        mid = l+(r-l)//2
        if arr[mid] < arr[mid+1]:       # for this condition the cur_element should be greater than the neighbours 
                                            # here if the cur_element is smaller than neighbour element that means the peak (element must be find at the right side so move l = mid + 1)
            l = mid + 1
        else:
            r = mid
    return r,l
print(peak_element([1,2,3,1]))
