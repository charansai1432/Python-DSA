#  remove duplicates in a sorted array using the fast and slow pointers

# template for the fast and slow pointer is 

# slow = 0 
# for i in range(n):
#     arr[slow] = arr[fast]
#     slow += 1
# return slow+1,arr


# brute force approach 

def remove_duplicates_in_a_sorted_array(arr):
    uniq = set()
    dup = []
    for num in arr:
        if num in uniq:
            dup.append(num)
        uniq.add(num)
    return len(uniq)
print(remove_duplicates_in_a_sorted_array([1,1,2,2,3]))

#  to remove duplicates in a sorted array 
#  The 1st element in the array is always unique only 

# the condition to check for the duplicates in the fast & slow pointer is 

#  if arr[f] != arr[s]  => slow += 1 ==> arr[s] = arr[f]  

#  arr,s+1

# optimal solution approach 

def remove_duplicates_in_sorted_array(arr):
    
    slow =  0 
    for fast in range(len(arr)):
        
        if arr[fast] != arr[slow]:              # condition which give the unique element  { her the 1st element is always unique}
            slow += 1                                   # such that 1st we move the slow += 1 ==> slow pointer '1' step forward to check for duplicates
            arr[slow] = arr[fast]           # after that we write with the slow pointer 

    return slow +1
print(remove_duplicates_in_sorted_array([1,1,2,2,3]))


def remove_duplicates_in_sorted_array(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1,arr
print(remove_duplicates_in_sorted_array([1,2,2,3,3,4,5]))


