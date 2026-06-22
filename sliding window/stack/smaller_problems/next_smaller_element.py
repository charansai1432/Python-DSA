# Question

# Given:

# arr = [4,8,5,2,25]

# For every element find:

# First {"Smaller'} Element on RIGHT side

# brute force approach 
def next_smaller_element(arr):
    n = len(arr)
    result = [-1]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break
    return result
print(next_smaller_element([4, 8, 5, 2, 25]))   #[2, 5, 2, -1, -1] 

# optimal solution approach 
def next_smaller_element(arr):
    n = len(arr)
    stack = []
    result = [-1]*n
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
print(next_smaller_element([4,8,5,2,25]))
