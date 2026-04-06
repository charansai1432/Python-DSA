# arr = [2, 1, 1, 1]
# k = 2

# 👉 Question:
# How many subarrays have sum = 2?

#optimal approach 
def count_subarrays_sum_eq_k(arr,k):
    cur_sum = 0
    count = 0
    freq = {0:1}    # IN {sum : how many times it repeated } ==> intitally sum = 0 repeated once (1) we assumed that (EDGE CASE)
                        #in this question to count the subarray's we store the hashmap with respective to the sum and hwo many times the sum is repeated {0:1} i.e sum zero has appread once 
                       # and we taking  that {0:1} at start 
                       
    #  freq = {}        # if we take like this Then the sub array at sum = 0 (is missed)    (SO CONSISTENT HAPPENS WE LOOSE THAT SUB ARRAY)                 
    n = len(arr)
    
    for i in range(n):
        cur_sum += arr[i] 
        past_sum = cur_sum - k      # if the cur_sum - k gives '0' then we can directly the calculate the sum and how it's repeaeted 
                                    # Here we pre-defined directly {0:1}
        
        if past_sum in freq:        # here the past_sum is seen we increase the count with the sum associate in the hashmap
            count += freq[past_sum]
            
            
            
        # if cur_sum not in freq:       # here we are not writing code like this because assume if cur_sum = 2 and freq{0:1} if 2 not in freq freq[2] += 1 
        #     freq[cur_sum] += 1        freq[2] doesn’t exist yet
                                        # 👉 You’re trying to increment something that isn’t there
                                        # Even deeper issue (logic mistake)

                                        # Even if Python didn’t crash, the logic is still wrong.

                                            # You wrote:

                                        # “If cur_sum not in freq → then increase”

                                        # But actually we need:

                                        # 👉 “Whether it exists or not, always update frequency”

                                        # Because:

                                        # If not present → set to 1
                                        # If present → increment count
#                                        🔹 Correct fix

#                                            Replace your last part with:

#                                                   freq[cur_sum] = freq.get(cur_sum, 0) + 1
        
        freq[cur_sum]  = freq.get(cur_sum,0)+1      #Here  we increment the cur_sum frequency ookk {2:1} for example at iteration and {2:2} => in 2nd iteration it become cur_sum frequency 2
            
    return count
print(count_subarrays_sum_eq_k([2, 1, 1, 1],2)) #3



# freq = “how many times have I seen this sum”
# You must not lose duplicates
# That’s why we increment, not just assign