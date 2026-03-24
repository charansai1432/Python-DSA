#brute force approach

def longest_equal_subarray(s,k):
    n = len(s)
    max_len = 0
    from collections import defaultdict
    for i in range(n):
        max_freq = 0
        freq = defaultdict(int)
        for j in range(i,n):
            freq[s[j]] += 1
            max_freq = max(max_freq,freq[s[j]])
            
            if (j-i+1) - max_freq == k:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_equal_subarray([1,2,1,1,3],1))    #4
        

#optimal solution 

def longest_equal_subarray(s,k):
    
    freq = {}
    max_len = 0
    max_freq =0
    l = 0 
    
    for r in range(len(s)):
        
        char = s[r]
        freq[char] = freq.get(char,0)+1
        max_freq = max(max_freq,freq[char])
        
        while (r-l+1) - max_freq > k:
            
            freq[s[l]] -= 1
            
            if freq[s[l]] == 0:
                del freq[s[l]] 
            
            l += 1
        max_len = max(max_len,r-l+1)
    return max_len
print(longest_equal_subarray([1,2,1,1,3],1))
        