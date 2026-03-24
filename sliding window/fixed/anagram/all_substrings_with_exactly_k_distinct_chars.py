
# Here this is question of fixed sliding window because here size is given i.e size k = 3

# why not varible size 

# reason -> in the question they will give all_substring_with_exactly_k_distinct_chars ==> varaible size
# reason -> in the question they will given all substrings with size k and distinct chars ==> here size is given so ==> fixed sliding window  (IMP ==  in the question itself they size , k= something then only it is fixed sliding window )

#brute force approach

def all_substrings_with_exactly_k_distinct_chars(s,k):
    
    result = []
    
    for i in range(len(s) - k +1):
        
        sub = s[i:i+k]
        ans = len(set(sub))
        
        if ans == k:
            result.append(i)
    return result
print(all_substrings_with_exactly_k_distinct_chars("abcabc",3)) #[0,1,2,3]

# optimal approach 

def all_substrings_with_exactly_k_distinct_chars(s,k):
    from collections import Counter
    n = len(s)
    
    result = []
    
    w_count = Counter()
    
    for i in range(n):
        
        w_count[s[i]] += 1
        
        if i >= k:
            w_count[s[i-k]] -= 1
            
            if w_count[s[i-k]] == 0:
                del w_count[s[i-k]]
                
        if i >= k - 1:
            
            if len((w_count)) == k:
                result.append(i-k+1)        #starting position i-k+1 window_starting position 
    return result
print(all_substrings_with_exactly_k_distinct_chars("abcabc",3))     #[0,1,2,3]
            