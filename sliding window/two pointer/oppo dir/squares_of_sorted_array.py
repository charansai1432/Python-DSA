# “You’re given a sorted array of integers (can include negative numbers). Return a new array containing the squares of each number, also in sorted order.”

# 🔍 Example
# Input:  [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

# 🧠 How to IDENTIFY pattern
# ✅ Array is sorted
# ❗ BUT negatives exist → sorted order breaks after squaring
# ✅ Largest values come from ends

# 👉 That’s your trigger:

# “I should compare left and right”

# 📏 Constraints Insight
# n up to 10⁵ → O(n log n) (sorting) is OK but not optimal
# Expected → O(n)


####################
#############    BRUTE FORCE APPROACH     ############

def squares_of_sorted_array(arr):
    
    result = []
    
    for num in arr:
        prod = abs(num**2)
        result.append(prod)
    result.sort()
    return result
print(squares_of_sorted_array([-4, -1, 0, 3, 10]))


# optimal solution   

# Here in the question they asked for the sorted array that means ascending order 
# that's why we used the pos = -1 which helps to  insert the bigger square from the ending of the list 
# here if i use the pos = 0 and pos += 1 which cause the array in the descending order after that we have to sort the array to acheive what asked in the question 
# so pos = 0 and pos += 1 which causes the elements to insert from the beginning 

def squares_of_sorted_array(arr):
    n = len(arr)
    l = 0
    r = n - 1
    pos = -1
    result = [0]*n
    
    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            
            result[pos] = arr[l]**2
            l += 1
        else:
            result[pos] = arr[r]**2
            r -= 1
        pos -= 1
        
    return result
print(squares_of_sorted_array([-4, -1, 0, 3, 10]))      #TC => O(n)
