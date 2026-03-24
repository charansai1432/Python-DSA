#brute force approac 

def longest_char_replacement_k_times(s,k):
    max_len = 0
    n = len(s)
    from collections import defaultdict
    
    for i in range(n):
        freq = defaultdict(int)
        
        max_freq = 0
        
        for j in range(i,n):
            freq[s[j]] += 1
            
            max_freq = max(max_freq,freq[s[j]])
            
            if (j-i+1) - max_freq <= k:
                max_len = max(max_len,j-i+1)
    return max_len
    
print(longest_char_replacement_k_times("AABABBA",1))    #4

#optimal solution 

def longest_char_replacement_k_times(s,k):
    l = 0
    max_len = 0
    freq = {}
    max_freq = 0
    for r in range(len(s)):
        char = s[r]
        
        freq[char] = freq.get(char,0)+1
        
        max_freq = max(max_freq,freq[char])
        
        while (r-l+1) - max_freq > k:
            freq[s[l]] -= 1
            
            if freq[s[l]] == 0:
                del freq[s[l]]
            l +=1
        max_len = max(max_len,r-l+1)
    return max_len
print(longest_char_replacement_k_times("AABABBA",1))