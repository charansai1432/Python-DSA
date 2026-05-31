
# brute force approach 

def remove_all_even_numbers(arr):
    odd_nums = []
    for num in arr:
        if num % 2 == 1:
            odd_nums.append(num)
    return len(odd_nums)
print(remove_all_even_numbers([2,3,4,5,6]))


# optimal solution approach 

def remove_all_even_numbers(arr):           # remove all even means ==> keep only odd numbers in array 
    
    n = len(arr)
    slow = 0
    for fast in range(n):
        if arr[fast] % 2 == 1:              # standard template 
            arr[slow] = arr[fast]
            slow += 1
    return slow
print(remove_all_even_numbers([2,3,4,5,6]))