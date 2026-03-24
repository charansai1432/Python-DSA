#brute force approach 

from collections import defaultdict

def longest_substring_atmost_k_distinct_chars(s,k):
    n = len(s)
    max_len = 0
    
    for i in range(n):
        freq = defaultdict(int)
        for j in range(i,n):
            freq[s[j]] += 1
            
            if len(freq) <= k:
                max_len = max(max_len,j-i+1)
    return max_len


print(longest_substring_atmost_k_distinct_chars("eceba",2))  #3


#optimal solution 

def longest_substring_with_atmost_k_distinct_chars(s,k):
    l = 0
    freq = {}
    max_len = 0 
    
    for r in range(len(s)):
        
        char = s[r]
        
        freq[char] = freq.get(char,0)+1
        
        while len(freq) > k :
            
            freq[s[l]] -= 1
            
            if freq[s[l]] == 0:
                del freq[s[l]]
                
            l += 1
        max_len = max(max_len,r - l + 1)
    return max_len
print(longest_substring_with_atmost_k_distinct_chars("eceba",2)) #3