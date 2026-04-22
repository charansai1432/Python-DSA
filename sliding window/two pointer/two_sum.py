
# brute force approach 

def two_sum(arr,target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return [i,j]
    return -1
print(two_sum([2,7,11,15],9))       #[0,1]


# optimal solution 

def two_sum(arr,target):
    freq = {}
    n = len(arr)
    for i,cur_num in enumerate(arr):
        past_num = target - cur_num
        if past_num in freq:
            return [freq[past_num],i]
        if cur_num not in freq:
            freq[cur_num] = i
    return -1
print(two_sum([2,7,11,15],9))     #[0,1]      #TC=> O(n)


# using two pointer here if the arr is sorted then it is applicable other wise we have to sort the array

def two_sum(arr,target):
    l = 0 
    r = len(arr) - 1
    
    while l < r:
        cur_sum = arr[l] + arr[r]
        if cur_sum == target:
            return [l,r]
        elif cur_sum < target:
            l+= 1
        else:
            r-= 1
    return -1
print(two_sum([2,7,11,15],9))       #[0,1]


# other wise the array isn't sorted we have to sort that one 1st

def two_sum(arr,target):
    
    arr = [(i,num) for i,num in enumerate(arr)]
    
    arr.sort()
    
    l = 0 
    r = len(arr) - 1
    
    while l < r:
        cur_sum = arr[l][1] + arr[r][1]
        if cur_sum == target:
            return [arr[l][1],arr[r][1]]
        elif cur_sum < target:
            l += 1
        else:
            r -= 1
    return -1
    
    
    
print(two_sum([2,7,15,11],9))       #[2,7]  TC=> O(n)