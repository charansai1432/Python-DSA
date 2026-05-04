# brute force approach 

def move_zeros(arr):
    non_zeros =[]
    zeros = []
    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    return non_zeros + zeros
    
print(move_zeros([0,1,0,3,12]))


# optimal solution approach 

def move_zeros(arr):
    
    slow = 0
    for fast in range(len(arr)):
        
        if arr[fast] != 0:
            arr[slow],arr[fast] = arr[fast],arr[slow]
            slow += 1
            
    return arr
print(move_zeros([0,1,0,3,12]))