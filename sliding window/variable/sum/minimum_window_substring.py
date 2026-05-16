
# brute force approach 

def minimum_window_string(s,t):
    from collections import Counter
    t_count = Counter(t)
    n = len(s)
    answer = ""
    min_len = float('inf')
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            substring_count = Counter(substring)
            valid = True
            for char in t_count:
                if substring_count[char] < t_count[char]:
                    valid = False
                    break
            if valid:
                if len(substring) < min_len:
                    min_len = len(substring)
                    answer = substring
    return answer,min_len
# print(minimum_window_string("ADOBECODEBANC","ABC"))

# optimal solution approach 
def minimum_window_string(s, t):

    from collections import Counter

    w_count = Counter()

    t_count = Counter(t)

    answer = ""

    min_len = float('inf')

    l = 0

    for r in range(len(s)):

        w_count[s[r]] = w_count.get(s[r],0)+1

        while True:

            valid = True

            # Check validity
            for char in t_count:

                if w_count[char] < t_count[char]:

                    valid = False

                    break

            # # Stop shrinking if invalid
            if not valid:
                break

            w_len = r - l + 1

            # Update answer
            if w_len < min_len:

                min_len = w_len

                answer = s[l:r+1]

            # Shrink window
            w_count[s[l]] -= 1

            if w_count[s[l]] == 0:
                del w_count[s[l]]

            l += 1

    return answer


# print(minimum_window_string("ADOBECODEBANC", "ABC"))



# brute force and optimal solution practise once again 

# brute force apporach --> generating all sub strings and check validity with the 't' string and if valid check which is the minimum length string and print the smallest sub string

def minimum_window_substring(s,t):
    n = len(s)
    answer = ""
    from collections import Counter
    t_count = Counter(t)
    min_len = float('inf')
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            substring_count = Counter(substring)
            
            # check validity with the t string with the substring_count
            valid = True
            for char  in t_count:
                if substring_count[char] < t_count[char]:
                    valid = False 
                    break
            if valid:
                if len(substring) < min_len:
                    min_len = len(substring)
                    answer = substring
    return answer,min_len
# print(minimum_window_substring("ADOBECODEBANC", "ABC"))


# optimal solution approach using the variable sliding window technique 


# previously we have see questions like -->  in the variable SW like 

# 1. Intialize 
# 2. Window_invalid condition -> shrink 
# 3. Update answer 

# the above technique is  valid for only the question longest , sum <= k , without repeating chars question 


######## but for the minimum window substring question we follow the different approach like 

# 1. intitalize 
# 2. while valid condition 
# 3 . update answer 
# 4. shrink 

# the above technique is only used the variable SW of minimum, sum >= k , minimum sum subarray (not kadane's) exact question i didnt remember related questions 


# optimal solution approach 

def minimum_window_substring(s,t):
    
    n = len(s)
    from collections import Counter
    t_count = Counter(t)
    answer = ""
    min_len = float('inf')
    l = 0
    freq = Counter()
    for r in range(n):
        
        freq[s[r]] = freq.get(s[r],0)+1
        
        valid = True 
        
        while True:                    # we dont when we can able to get the min_len substring so iterate over the string until a valid min_len is found 
            
            # check for the valid string 
            for char in t_count:
                if freq[char] < t_count[char]:      # for invalid string logic 
                    valid = False
                    break 
                # ok for suppose if 1 char have freq = 0 then that means 0 < 1 condition is true then valid = false break from the for loop now 
                # now It will check in the if not false => True => if codition is true => break which eventually exits from the current substring loop no more shirnking because already the substring doesnt have the required chars even if we shrink we cannot the required no. of char presnt in the 't' string
            
            
            # below if valid is used for invalid string and valid string too 
            if not valid:       # if valid = True => then not valid is False ==> that means if condition is False 
                                    # then we find a valid string now we have to check for the min_len string if min_len is found in substring  then return the answer
                break
            
            win_len = r - l + 1
            if win_len < min_len:
                min_len = r - l + 1         
                # answer update same as above i discussed the template for variable SW in minimum way
                
                answer = s[l:r+1]           # genrally we do slicing the string na like that only 
                                                        # l = 0 , r + 1 => from index postion to r + 1 => entire string 
                
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l+= 1
            
    return answer,min_len
# print(minimum_window_substring("ADOBECODEBANC", "ABC"))

# the above approach will make into the time complexity of O(n*m) = > n = len(s) and m = len(t)

# In simple terms  here we check every time entire hashmap for every substring which the makes the time complexity even more 

############################ O(N) ############## approach 
# so the best approach is maintaing the have and need technique which makes the time complexity as O(n)

# optimal solution with O(n) technique

def minimum_window_substring(s,t):
    n = len(s)
    min_len = float('inf')
    answer = ""
    have = 0
    from collections import Counter
    t_count = Counter(t)
    need = len(t_count)         # which gives 
    freq = {}
    l = 0
    for r in range(n):
        freq[s[r]] = freq.get(s[r],0)+1
        
        # check for validity   # it's the condition for the valid window
        if s[r] in t_count and freq[s[r]] == t_count[s[r]]:
            have += 1
        
        while have == need:
            win_len = r - l + 1
            if win_len < min_len:
                min_len = win_len
                answer = s[l:r+1]
            
            freq[s[l]] -= 1
            
            if s[l] in t_count and freq[s[l]] <t_count[s[l]]:        # for invalid window checking condition 
                have -= 1
            l+=1
    return answer,min_len
print(minimum_window_substring("ADOBECODEBANC", "ABC"))

                        
    
    


