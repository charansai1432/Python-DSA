

# brute force approach

def previous_smaller_element(arr):
    n = len(arr)
    result = [-1]*n
    for i in range(n):
        for j in range(i-1,-1,-1):
            if arr[j] < arr[i]:
                result[i]=arr[j]
                break
    return result
print(previous_smaller_element([4, 10, 5, 8, 20]))      # [-1, 4, 4, 5, 8]


# optimal solution approach 

def previous_smaller_element(arr):
    n = len(arr)
    stack = []
    result = [-1]*n
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result
print(previous_smaller_element([4, 10, 5, 8, 20]))      #[-1, 4, 4, 5, 8]

