#brute force approach

def count_anagram_substring(s,p):
    
    k = len(p)
    from collections import Counter
    p_count = Counter(p)
    count = 0
    
    for i in range(len(s)):
        
        substr = s[i:i+k]
        
        if Counter(substr) == p_count:
            count += 1 
            
    return count
print(count_anagram_substring("forxxorfxdofr","for"))   #3



# optimal approach

def count_anagram_substring(s,p):
    from collections import Counter 
    k = len(p)
    count = 0
    P_count = Counter(p)
    w_count = Counter()
    
    for i in range(len(s)):
        w_count[s[i]] += 1
        
        if i >= k:
            w_count[s[i-k]] -= 1
            
            if w_count[s[i-k]] == 0:
                del w_count[s[i-k]]
                
        if i >= k - 1:
            if w_count == P_count:
                count += 1
    return count
    
print(count_anagram_substring("forxxorfxdofr","for"))   #3
        