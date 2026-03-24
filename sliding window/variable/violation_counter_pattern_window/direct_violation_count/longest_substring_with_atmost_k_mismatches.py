#brute force
def longest_substring_with_atmost_k_mismatches(s,t,k):
    max_len = 0
    n = len(s)
    for i in range(n):
        
        mis_match = 0
        for j in range(i,n):
            if s[j] != t[j]:
                mis_match += 1
            
            if mis_match <= k:
                max_len = max(max_len,j-i+1)
    return max_len
        
print(longest_substring_with_atmost_k_mismatches("abcd","bcdf",1))      #1

#optimal solution 

def longest_substring_with_atmost_k_mismatches(s,t,k):
    
    max_len = 0
    mis_match = 0
    l = 0 
    
    if len(s) != len(t):
        return 0
    
    for r in range(len(s)):
        
        if s[r] != t[r]:
            mis_match += 1
            
        while mis_match > k:
            
            if s[l] != t[l]:
                mis_match -= 1
            l+=1
            
        max_len = max(max_len,r-l+1)
    return max_len
    
    
print(longest_substring_with_atmost_k_mismatches("abcd","bcdf",1)) #1