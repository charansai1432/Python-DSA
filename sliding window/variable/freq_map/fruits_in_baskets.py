#brute force approach

from collections import defaultdict

def fruits_in_baskets(arr,k):
    
    max_len = 0
    n = len(arr)
    
    for i in range(n):
        
        freq = defaultdict(int)
        
        for j in range(i,n):
            freq[arr[j]] += 1
            
            if len(freq) <= k:
                max_len = max(max_len,j-i+1)
    return max_len

print(fruits_in_baskets([1,2,1,2,3,2,2],2))  #4


#optimal solution 

def fruits_in_baskets(arr,k):
    
    l = 0 
    max_len = 0 
    freq = {}
    
    for r in range(len(arr)):
        
        char = arr[r]
        
        freq[char] = freq.get(char,0)+1
        
        while len(freq) > 2:
            freq[arr[l]] -= 1
            
            if freq[arr[l]] == 0:
                del freq[arr[l]] 
            l+=1
        max_len = max(max_len,r-l+1)
    return max_len 
     
print(fruits_in_baskets([1,2,1,2,3,2,2],2))