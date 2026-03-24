# brute force approach

def permutation_in_string(s1,s2):
    from collections import Counter
    n = len(s2)
    s2_count = Counter(s2)
    
    k = len(s1)
    
    for i in range(n-k+1):
        
        sub = s2[i:i+k]
        
        if Counter(sub) == Counter(s1):
             return True
        
    return False 
            
print(permutation_in_string("ab","eidbaooo"))   #True

#optimal approach

def permutation_in_string(s1,s2):
    
    k = len(s1)     #pattern=>p ->s1
    from collections import Counter
    s1_count = Counter(s1)
    
    w_count = Counter()
    
    for i in range(len(s2)):
        
        w_count[s2[i]] += 1
        
        if i >= k:          #shrink logic for  fixed SW 
            
            w_count[s2[i-k]] -= 1
            
            if w_count[s2[i-k]] == 0:
                del w_count[s2[i-k]]
                
        if i >= k-1:
            if w_count == s1_count:
                return True
    return False
print(permutation_in_string("ab","eidbaooo"))   #True
            
    
    