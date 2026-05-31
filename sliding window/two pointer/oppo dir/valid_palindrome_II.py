

# Problem: Valid Palindrome II
# 🧾 Question

# You can delete at most one character. Check if string can be palindrome.

# 🧠 Pattern
# Opposite pointer
# When mismatch → try skipping left OR right

#  This is the question in a string ==> we have to remove a one character and check whether it is a palindrome or not 

#  to remove that one char in a string we can simple move the left and right pointer by '1' step forward for left and right  pointer 

# brute force approach 

def valid_palindrome_II(s):
    
    if s == s[::-1]:
        return True
    
    def valid_palindrome(s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return valid_palindrome_II(s[l+1:r+1]) or valid_palindrome_II(s[l:r])
            l += 1
            r -= 1
        return True
    print(valid_palindrome("abca"))