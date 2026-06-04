# brute force approach 

def aggressive_cows_bruteforce(stalls, cows):

    stalls.sort()

    answer = 1

    max_distance = stalls[-1] - stalls[0]

    for distance in range(1, max_distance + 1):

        cows_placed = 1

        last_position = stalls[0]

        for i in range(1, len(stalls)):

            if stalls[i] - last_position >= distance:

                cows_placed += 1

                last_position = stalls[i]

        if cows_placed >= cows:

            answer = distance

    return answer


print(aggressive_cows_bruteforce([1,2,4,8,9], 3))      # 3

# print(aggressive_cows_bruteforce([10,1,2,7,5], 3))     # 4

# print(aggressive_cows_bruteforce([1,2,3,4,5], 2))      # 4


#This is the question where in the previous questions we have seen that "F,F,F,T,T,T" pattern in the "COWS" question we can see the pattern "T,T,T,T,F,F,F,F"
# so in this pattern like [T,T,T,F,F,F] => HERE we take the Last True value 

#In this question
# 1. first we have to the "SORT" the stalls.
# 2. Here the actuall question we have to place the cows that "NO ONE COW FIGHT WITH EACH OTHER" 
#  3. so the minimum distance is 1 
#  4. max distance = last_stall_postion - cur_stall_position        {simple like distance formula is math}
#  5. here we have to fix the first stall position as lastpostion 
# 6. by using that last position value we can able to find out the distance between any cows should be >= max_distance 

#  "THIS is the pattern where return <= { becomes the >= i.e T,T,T,F,F,F}" pattern 
# In the previous question we  find the minimum answer 
# but in this question we find the maximum answer 


# optimal solution 

def agressive_cows(stalls,cows):
    stalls.sort()
    def possible(max_distance):
        cows_placed = 1
        last_position = stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i] - last_position >= max_distance:
                cows_placed += 1
                last_position = stalls[i]
        return cows_placed >= cows
    
    l = 1                                       # The minimum distance between any 2 cows is "1"
    r = max(stalls) - min(stalls)                   # the distance b/w any 2 cows is max(stall) - min(stall) which gives the search space for us 
    answer = r
    while l <= r:
        mid = l +(r-l)//2
        if possible(mid):
            answer = mid 
            l = mid + 1                         # l = mid + 1 which gives the max_answer that we can place the cows far from each other 
                                                        # why ? => as array is sorted moving right side which gives the max_answer
        else:
            r = mid - 1
    return answer
print(agressive_cows([1, 2, 4, 8, 9],3))            #3

print(agressive_cows( [10, 1, 2, 7, 5],3))          #4