
# brute force approach

def three_sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == target:
                    return [i,j,k]
    return -1
print(three_sum( [-1, 0, 1, 2, -1, -4],0))