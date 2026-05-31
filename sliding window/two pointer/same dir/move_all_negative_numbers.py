# brute force approach 

def move_all_negative_numbers(arr):
    neg_ele = []
    non_neg_ele = []
    for num in arr:
        if num < 0:
            neg_ele.append(num)
        else:
            non_neg_ele.append(num)
    return neg_ele + non_neg_ele
print(move_all_negative_numbers([1,-2,3,-4,5]))


# optimal solution approach 

def move_all_negative_numbers(arr):             # move all neg elements to start ==> and positive numbers to end  
    n = len(arr)
    slow = 0
    for fast in range(n):
        if arr[fast] < 0:                   # if cur_element is less than '0' then swap it 
            arr[slow],arr[fast]= arr[fast],arr[slow]
            slow += 1
    return slow,arr
print(move_all_negative_numbers([1, -2, 3, -4, 5]))     # (2, [-2, -4, 3, 1, 5])