

# brute force approach 

def daily_temperatures(arr):
    n = len(arr)
    result = [0]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                result[i] = j - i 
                break
    return result
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))     #[1, 1, 4, 2, 1, 1, 0, 0]


# optimal solution approach 

def daily_temperatures(arr):
    n = len(arr)
    stack = []
    result = [0]*n
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))     #[1, 1, 4, 2, 1, 1, 0, 0]