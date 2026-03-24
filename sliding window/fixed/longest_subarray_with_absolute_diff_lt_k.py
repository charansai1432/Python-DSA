#optimal solution

# in any question if absolute difference is asked this is the formula for that

# (max element in window) - (min element in window) <= k

# This question is of varaible sliding window => longest substring + condition (absolute diff <= k) ===> variable SW

# peviosuly we have practise for the max,min of a window in FIXED SW using dequqe technique 

# Below is for varaible SW ==> using dequqe technique sligthly different from FIXED SW ==> because the WINDOW SIZE isn't fixed (IMPORTANT)

# That's why we keep the popleft() function in the down while loop and the condition max_dq[0] == j => max_dq.popleft()  ====> mainly used in the variable size (DEQUE)

def longest_subarray_with_absolute_diff_lt_k(arr,k):
    
    max_len = 0 
    from collections import deque
    
    max_dq = deque()
    min_dq = deque()
    
    result = []
    j = 0
    n= len(arr)
    count = 0
    
    for i in range(n):
        # window_start = i - k + 1
        
        # if max_dq and max_dq[0] < window_start:           #here all the commented lines are only used for the fixed sliding window 
                                                            # Here the question is variable SW => the commented lines are only for the fixed Sw
                                                            
        #     max_dq.popleft()
            
        # if min_dq and min_dq[0] < window_start:
        #     min_dq.popleft()
            
        while max_dq and arr[max_dq[-1]] < arr[i]:
            max_dq.pop()                            #we get the max_element fro this conditions
            
        while min_dq and arr[min_dq[-1]] > arr[i]:
            min_dq.pop()                            #we get the min_element for this conditions
            
        max_dq.append(i)
        min_dq.append(i)
        
        while (arr[max_dq[0]] - arr[min_dq[0]]) > k:    # Window INVALID case taken (because it's a variable size sliding window) 

            if max_dq[0] == j:
                max_dq.popleft()            # This lines of code is for the varaible Sw using DEQUE => like if max_dq[0] == j (here j is intially '0' ) 
            if min_dq[0] == j:
                min_dq.popleft()
                
            j += 1                          # In gerenral variable sliding window we increase the left pointer right SAME here too i.e l+=1
            
        if (i-j+1) > max_len:           # to check the all valid windows => and to generate the valid window of highest window length 
            
            max_len = i-j+1  # max_len => how long window is 
            
            start = j               # start means where the actual window begins i.e j = 0 ASSUME the window begins from here 
            
        count += i-j+1              # count no. of subarray's 
        
        max_len = max(max_len,i-j+1)    #longest length subarray 
        
    return count,max_len,arr[start:start+max_len]       # returning the which subarray is largest 

print(longest_subarray_with_absolute_diff_lt_k([8,2,4,7],4))