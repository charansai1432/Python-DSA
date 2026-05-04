
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


# optimal solution approach 

def remove_duplicates_in_sorted_array(arr):
    
    slow =  0 
    for fast in range(len(arr)):
        
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
            
    return slow +1
print(remove_duplicates_in_sorted_array([1,1,2,2,3]))