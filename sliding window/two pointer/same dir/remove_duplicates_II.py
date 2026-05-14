# # Given a sorted array, remove duplicates in-place such that each element appears at most twice. 
# # Return the new length.”


# Input:  [1,1,1,2,2,3]
# Output: 5
# Array:  [1,1,2,2,3,...]


# brute force approach 

def remove_duplicates(arr):
    freq = {}
    uniq = []
    for num in arr:
        freq[num] = freq.get(num,0)+1
        if freq[num] <= 2:
            uniq.append(num)
    return uniq
print(remove_duplicates([1,1,1,2,2,3]))


# optimal solution using the fast & slow pointers

def remove_duplicates(arr):
    slow = 2                                    # first two elements are always valid i.e the 1st 2 are always unique
    for fast in range(2,len(arr)):
        if arr[fast] != arr[slow-2]:
            arr[slow] = arr[fast]
            slow += 1
    return slow,arr
print(remove_duplicates([1,1,1,2,2,3]))


## IMPORTANT ##

# Here the remove_duplicates atmost k problem 

            # have the formula like slow - k 