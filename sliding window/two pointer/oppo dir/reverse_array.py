

# brute force approach 

def reverse_array(arr):
    
    arr.reverse()                       #Creates new array (extra space)
    return arr                      
print(reverse_array([1,2,3,4,5]))       #TC=> O(n) and sc=> (n)

# brute force approach again 

def reverse_array(arr):
    return arr[::-1]                        #Creates new array (extra space)
print(reverse_array([1,2,3,4,5]))               # tc=> O(n) and sc => O(n)

# optimal solution approach

def reverse_array(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r -= 1
    return arr
print(reverse_array([1,2,3,4,5]))           # tc => O(n) and sc => O(1)