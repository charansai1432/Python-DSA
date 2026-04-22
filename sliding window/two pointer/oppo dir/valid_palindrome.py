# “Check if a string reads the same forward and backward.”

# Example
# Input: "madam"
# Output: True

# Input: "hello"
# Output: False

# Pattern Identification

# Comparing first and last
# Then second and second-last

# 👉 This is also Opposite Direction Two Pointer

# brute force approach

def valid_palindrome(s):
    
    return s == s[::-1]             # here s[::-1] this creates a copy of list which leads to a copy of a list

print(valid_palindrome("madam"))


# optimal solution 

def valid_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True
    
    
print(valid_palindrome("madam"))