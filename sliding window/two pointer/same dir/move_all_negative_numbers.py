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

def move_all_negative_numbers(arr):
    n = len(arr)
    slow = 0
    for fast in range(n):
        if arr[fast] < 0:
            arr[slow],arr[fast]= arr[fast],arr[slow]
            slow += 1
    return slow,arr
print(move_all_negative_numbers([1, -2, 3, -4, 5]))