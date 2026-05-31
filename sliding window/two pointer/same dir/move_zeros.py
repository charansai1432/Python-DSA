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

def move_zeros(arr):                            # move_zero's to end means == > starting having only numbers 
    
    slow = 0
    for fast in range(len(arr)):
        
        if arr[fast] != 0:              # this condition tells if the cur_element is not zeros swap that one 
            arr[slow],arr[fast] = arr[fast],arr[slow]           # using this logic we can able swap it and maintain the zeros at end.
            slow += 1
            
    return arr
print(move_zeros([0,1,0,3,12]))