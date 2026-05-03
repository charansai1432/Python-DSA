
#brute force approach 

def four_sum(arr,total):
    n = len(arr)
    result = []
    arr.sort()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[k] == total:
                        result.append([arr[i],arr[j],arr[k],arr[l]])
    return result
print(four_sum([1,2,3,4,5,0,0,0],0))

# optimal solution approach

def four_sum(arr,target):
    n  = len(arr)
    result = []
    arr.sort()
    for i in range(n-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            
            l = j + 1
            r = n - 1
            while l < r:
                total = arr[i] + arr[j] + arr[l] + arr[r]
                
                if total == target:
                    result.append([arr[i],arr[j],arr[l],arr[r]])
                    l+=1
                    r-=1
                    
                while l < r and arr[l] == arr[l-1]:
                    l += 1
                while l < r and arr[r] == arr[r + 1]:
                    r -= 1
                if total < target:
                    l += 1
                else:
                    r -= 1
    return result

print(four_sum([1,2,3,4,5,5,6,6],6))
        