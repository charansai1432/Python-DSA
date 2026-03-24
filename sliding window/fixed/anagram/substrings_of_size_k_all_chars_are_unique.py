#brute force approach

def substring_of_size_k_all_chars_are_unique(s,k):
    
    n = len(s)
    result = []
    for i in range(n):
        
        sub = s[i:i+k]
        
        if len(set(sub)) == k:
            result.append(i)
    return result

print(substring_of_size_k_all_chars_are_unique("abcabcbb",3))      #[0,1,2,3]


# optimal  approach 

def substring_of_size_k_all_chars_are_unique(s,k):
    from collections import Counter
    
    n = len(s)
    result = []
    w_count = Counter()
    
    for i in range(n):
        w_count[s[i]] +=1
        
        if i>= k:
            w_count[s[i-k]] -= 1
            
            if w_count[s[i-k]] == 0:
                del w_count[s[i-k]]
                
        if i >= k-1:
            if len(set(w_count)) == k:
                result.append(i-k+1)
    return result

print(substring_of_size_k_all_chars_are_unique("abcabcbb",3))   #[0,1,2,3]