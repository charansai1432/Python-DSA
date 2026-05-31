# here in this question is actually like an ships,allocate books question only
 # the actual difference is the here arr = work to be assigned for the group of users
 # in a group no one worker should not exceed the max_work 
 
# optimal solution approach 

def split_array_largest_sum(work,k):
    
    def possible(max_largest_sum):
        
        cur_sum = 0
        groups_needed = 1
        for num in work:
            if cur_sum + num > max_largest_sum:         # i.e the cur_work + work should not exceed the max_work per worker 
                groups_needed += 1
                cur_sum = num
            else:
                cur_sum += num
                
        return groups_needed <= k
    
    l = max(work)               # here 'l' which gives the max(work) that a worker can do that gives the l pointer 
    r = sum(work)                       # the 'r' which gives the sum(work) that a group can do ==> gives the search space for me 
    answer = r                                  # here answer = r which gives the best answer from the max_val like that 
    while l <= r:
        mid = l + ( r - l)//2
        if possible(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer
print(split_array_largest_sum([7,2,5,10,8],2))
    
    
    
    
    