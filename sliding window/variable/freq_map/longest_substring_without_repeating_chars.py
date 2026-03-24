#brute force approach

from collections import defaultdict

def longest_substring_without_repeating_chars(s):
    max_len = 0
    n = len(s)
    
    for i in range(n):
        freq = defaultdict(int)
        for j in range(i,n):
            freq[s[j]] += 1
            
            if freq[s[j]] == 1:
                max_len = max(max_len,j-i+1)
    return max_len
            
print(longest_substring_without_repeating_chars("abcabcbb"))    #3


# optimal solution 


def longest_substring_without_repeating_chars(s):
    
    
    l = 0
    max_len  = 0
    freq = {}
    
    for r in range(len(s)):
        
        char = s[r]
        
        freq[char] = freq.get(char,0) + 1
        
        while freq[char] > 1:
            freq[s[l]] -= 1
            
            if freq[s[l]] == 0:
                del freq[s[l]]
            
            l += 1
        max_len = max(max_len,r - l +1)
    return max_len
print(longest_substring_without_repeating_chars("abcabcbb")) #3