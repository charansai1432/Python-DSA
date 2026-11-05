

#  question is -> we have to find the min_cost when attaching the two sticks... in the array also here each stick has to connect with each other while maintaing the minimum cost.

#  How to identify the question can be solved using the min_heap + greddy algo 
# 
# {VVVVIMP} Greddy-algo ==>  at every step we choose the best avaiable option .. which  will eventually leads to the optimal solution 

#     in this algo we have two type's of optium --> 1. local optimum , 2. global optium 

#  local optium is nothing .. At each step, we choose the best available option according to our greedy strategy
#  global optium ==> the best possible answer for the entire problem {or} locally optimal choices must lead to the globally optimal answer for Greedy to work correctly.

#  once a decision is made we cannot change it ==> greddy algo 

# pattern to identify the greddy algo 

# How to identify Greedy problems?
# This is the most important part for interviews.

# When you read a problem statement, look for these clues.
#           Clue 1: Minimum or Maximum
# Words such as:
# - Minimum cost
# - Maximum profit
# - Minimum operations
# - Maximum number of tasks
# - Minimum resources
# These suggest an optimization problem.

# But remember: minimum or maximum alone does not mean Greedy.
#               Clue 2: Make a choice at every step
# Ask yourself:

# "Can I solve this problem by making one best choice at a time?"

# For example:
# - Select the smallest element.
# - Select the largest profit.
# - Choose the earliest finishing activity.
# - Choose the nearest available option.
# If one local choice helps us move toward the final answer, Greedy may be suitable.

#                   Clue 3: The decision helps reduce the remaining problem
# Suppose you have:

# [2, 4, 6, 8]

# You need to repeatedly combine two smallest values.

# You select:

# 2 + 4 = 6

# Now the remaining problem becomes:

# [6, 6, 8]

# You have reduced the problem size by one element.

# This is a strong clue for a Greedy + Min Heap approach.

#                Clue 4: Previous decisions are not reconsidered
# Greedy generally commits to a decision.

# {VVVVIMP}If the problem requires trying many possible decisions and comparing their future outcomes, Greedy alone might not be sufficient.

# 

#  Actually question --> we have the list of sticks ... we have to find the minimum cost to {connect} all the sticks.
# 
# we get the minimum cost --> we will take the two smallest sticks in the list 
#  the cost is calucalted as the sum of two sticks ---> and the new stick means the first and second smallest stick has to be inserted back to main list.
#   here the add the two smallest sticks ... atleast two sticks has to be there ..
# 
#
# BF approach 

# Idea: Every time, search for the two smallest sticks, remove them, connect them, and insert the newly formed stick back into the list.

#  makes the time complexity to O(n2)
sticks = [1,3,5,7]

def minimum_cost_of_two_stick(sticks):
    
    min_cost = 0            # intial minimum cost before attaching any sticks 
    
    while len(sticks) > 1:              # to attach any two sticks ... there should atleast 2 sticks ..if atlast we have only 1 stick left we break the loop.
        
        first_min_stick = min(sticks)           # get's the 1st minimum stick value 
        sticks.remove(first_min_stick)
        
        second_min_stick = min(sticks)          # gets the 2nd minimum stick value 
        sticks.remove(second_min_stick)
        
        min_cost += second_min_stick + first_min_stick          # get the min_cost by adding the 1st_minimum_stick_value and 2nd minimum stick value 
        
        new_stick = first_min_stick + second_min_stick          # here a new stick is formed by the 1st and 2nd minimum stick value 
        
        sticks.append(new_stick)            # inserted the new stick value back the list 
    return min_cost

print(minimum_cost_of_two_stick(sticks))


#  the optimal solution can be done using the min_heap + greddy 

#  in the BF approach we will calucalte for the 1st and 2nd minimum stick value every time 

#  but in the optimal approach --> we use the min_heap ... which provides the smallest value every time using the heappop() function 

#  here where greddy is used ---> instead of calculating the  1st and 2nd minimum stick value every time  ...

#  we used a heap to make the best choice every time using the heappop() --> which directly gives teh  1st and 2nd minimum stick value ... instead of traversing the entire array 


# greddy algo template is 

# Greedy thinking template
#            1. Understand the goal
   
#    Identify whether you need minimum, maximum, or feasibility.
# 2.                Identify the greedy choice
   
#    Decide what is best at the current step.
# 3.                Make the choice
   
#    Select the best available option.
# 4.                Update the problem
   
#    Update the remaining values, state, or resources.
# 5.                Repeat
   
#    Continue until the stopping condition is reached.
# 6.             Return the answer
   
#Return the minimum cost, maximum profit, or required result.


#  the same for this question is actually 
# 1. we choose the best choice --> here by choosing the two smallest sticks --> we can maintain the min_cost ===> so this is the best choice 
#  2. after calucalting the min_cost .. we have again attach the sticks back to the heap ===> updation ==> (Update the problem after making a decision.)  => that's what we did in the heappush after the new stick --> best choice values has to be again placed back to the heap 
#  repeat  ==> We continue making decisions until the problem's stopping condition is satisfied. (stopping condition if only one stick is remained.)
#  return final answer 

# {VVVIMP}          {VVVVIMP}
# Greedy decides which two sticks to combine.

# Min Heap helps us quickly retrieve those two smallest sticks.

# optimal solution using the min_heap + greddy algo


# I would use a Greedy approach with a Min Heap. At every step, I extract the two smallest sticks, connect them, add their combined length to the total cost, and insert the newly formed stick back into the heap.
# I repeat this process until only one stick remains 
sticks = [1, 3, 5, 7]

def minimum_cost_of_two_sticks(sticks):
    import heapq 
    heapq.heapify(sticks)               # to apply min_heap here --> 1st we have change the list into the Min_heap usiing the heapify funtion 
    min_cost = 0 
    while len(sticks) > 1:          # attach the sticks only when having the atleast (2) sticks.
        
        first_smallest=heapq.heappop(sticks)        # which gives the 1st smallest stick 
        second_smallest = heapq.heappop(sticks)             # gives the 2nd smallest stick
        
        min_cost += first_smallest + second_smallest            # min cost calucalte 
        
        new_stick = first_smallest + second_smallest            # inserting the new stick back to the heap
        
        heapq.heappush(sticks,new_stick)
    return min_cost
print(minimum_cost_of_two_sticks(sticks))




# Important Greedy patterns you will encounter
# Don't study all these now. Just become familiar with their names.

# Pattern	Example problem

# Sorting + Greedy	Assign Cookies
# Interval Greedy	Non-overlapping Intervals
# Activity Selection	Maximum Number of Events
# Heap + Greedy	Minimum Cost to Connect Sticks
# Two Pointers + Greedy	Assign Cookies
# Greedy + Tracking Maximum	Jump Game
# Greedy + Graphs	Minimum Spanning Tree


