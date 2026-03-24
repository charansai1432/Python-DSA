#brute force approach

def find_anagram_in_s_from_p_return_indexs(s,p):
    
    from collections import Counter
    
    result = []
    k = len(p)
    n = len(s)
    P_count = Counter(p)
    
    for i in range(n-k+1):
        
        sub = s[i:i+k]
        
        if Counter(sub) == P_count:
            result.append(i)
    return result
    
print(find_anagram_in_s_from_p_return_indexs("cbaebabacd","abc")) #[0,6]




#optimal approach

def find_anagram_in_s_from_p_return_index(s,p):
    k = len(p)
    from collections import Counter
    p_count = Counter(p)
    
    w_count = Counter()
    
    result = []
    
    for i in range(len(s)):
        
        w_count[s[i]] += 1      #Insert the char freq into the w_count
        
        if i >= k:          # Remove logic 
            w_count[s[i-k]] -= 1        #s[i-k] => shrinking window logic in fixed Sw
            
            if w_count[s[i-k]] == 0:
                del w_count[s[i-k]]
            
        if i >= k - 1:          # valid window is formed ==> i.e after all the shrinking -> we compare the strings and return the result 
            
            if w_count == p_count:
                result.append(i-k+1)
    
    return result
print(find_anagram_in_s_from_p_return_index("cbaebabacd","abc"))  #[0,6]