#brute force approach

def longest_with_k_mismatchs(s,t,k):
    n = len(s)
    max_len = 0
    
    for i in range(n):
        mis_match = 0
        for j in range(i,n):
            if s[j] != t[j]:
                mis_match += 1
                
            if mis_match <= k:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_with_k_mismatchs("abcde","abfde",1))  #5


#optimal solution 

#for the both k mismatches or k errors in the question they are two Strings to compare the mismatches or error's

def longest_with_k_mismatchs(s,t,k):
    
    l = 0 
    max_len = 0
    mis_match = 0
    
    for r in range(len(s)):
        
        if s[r] != t[r]:
            mis_match += 1
            
        while mis_match > k:
            if s[l] != t[l]:
                mis_match -= 1
            l+=1
        max_len = max(max_len,r-l+1)
    return max_len
print(longest_with_k_mismatchs("abcde","abfde",1))