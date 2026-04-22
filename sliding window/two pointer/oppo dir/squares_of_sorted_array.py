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
#############        BRUTE FORCE APPROACH ############

def squares_of_sorted_array(arr):
    
    result = []
    
    for num in arr:
        prod = abs(num**2)
        result.append(prod)
    result.sort()
    return result
print(squares_of_sorted_array([-4, -1, 0, 3, 10]))


# optimal solution 
