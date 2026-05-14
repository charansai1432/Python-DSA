# minimum window substring 

# return the substring that contains the all char from t 

# s = "ABACAC"
# T = "AABC"

# Duplicates matter


#############        iDENTIFYING         ##################
# This question is varaible sliding window pattern question becuase in the question they didnt mention the size of k 
# and here we can't take it as fixed SW because t is fixed although the s doesn't has the fixed window right --> how ?? some times 
# the window can be 2 or 3 or 4 how ?? for each substrig it is differnt right 

# brute force approach

def minimum_window_substring(s,t):
    
    n = len(s)
    min_len = float('inf')
    from collections import Counter
    t_count = Counter(t)
    ans = ""
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            s_count = Counter(substring)
            valid = True
            for char in t_count:
                if s_count[char] < t_count[char]:
                    valid = False
                    break 
                
            if valid:                                   # valid has to True then only below statments will execute 
                
                if len(substring) < min_len:
                    min_len = len(substring)
                    ans = substring
                    
    return ans,min_len
print(minimum_window_substring("ADOBECODEBANC","ABC"))


# optimal solution using the variable SW

def minimum_window_substring(s,t):
    n = len(s)
    