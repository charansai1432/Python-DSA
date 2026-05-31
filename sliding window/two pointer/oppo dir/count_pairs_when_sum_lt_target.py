
#  this is the question we have to count the pairs where sum <= target ===> two pointer technique 

# array is sorted , condition , pairs or triplet

# brute force approach 

def count_pairs_when_sum_lt_target(arr,target):
    
    count = 0
    
    for i in range(len(arr)):
        # cur_sum = 0
        for j in range(i+1,len(arr)):
                if arr[i] + arr[j] < target:
            
            
                    count += 1
    return count
print(count_pairs_when_sum_lt_target([1,2,3,4],6))      #4
    
    
# optimal solution 

def count_pairs_when_sum_lt_target(arr,target):
    n = len(arr)
    l  = 0
    r = n - 1
    count = 0
    while l < r:
        cur_sum = arr[l] + arr[r]
        if cur_sum < target:
            count += (r-l)          # in the traditional variable Sw technique also we count like r - l +1 in the two pointer technique we use the r -l to count ==> count = (r-l)
            l += 1                      # even after finding the pair we move the l += 1 because the next 'l' value can also from a pair or not to check we increase the 'l' pointer forward 
        else:
            r -= 1
    return count
        
print(count_pairs_when_sum_lt_target([1,2,3,4],6))      #4
        