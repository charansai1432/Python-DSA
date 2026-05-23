
# brute force approach 

def peak_element(arr):
    n = len(arr)

    for i in range(n):

        left = float('-inf') if i == 0 else arr[i-1]
        right = float('-inf') if i == n-1 else arr[i+1]

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
        if arr[mid] < arr[mid+1]:
            l = mid + 1
        else:
            r = mid
    return r,l
print(peak_element([1,2,3,1]))
