#brute force approach 

from collections import defaultdict

def longest_substring_with_exactly_k_distinct_chars(arr,k):
    max_len = 0
    n = len(arr)
    
    for i in range(n):
        freq = defaultdict(int)
        
        for j in range(i,n):
            freq[arr[j]] += 1
            
            if len(freq) == k:
                max_len = max(max_len,j-i+1) 
    return max_len
print(longest_substring_with_exactly_k_distinct_chars("aabacbebebe",3)) #7


#optimal solution 

def longest_substring_with_exactly_k_distinct_chars(s,k):
    l = 0
    max_len = 0 
    
    freq= {}
    
    for r in range(len(s)):
        
        char = s[r]
        
        freq[char] = freq.get(char,0)+1
        
        while len(freq) > k:
            freq[s[l]] -= 1
            
            if freq[s[l]] == 0:
                del freq[s[l]]
            
            
            l += 1
        
        if len(freq) == k :
            max_len = max(max_len,r-l+1)

        
    return max_len
print(longest_substring_with_exactly_k_distinct_chars("aabacbebebe",3)) #7