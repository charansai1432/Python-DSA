# 
#  here the question is ==> we have to complete the all tasks with the minimum amount of time 
# The task's can be done in any order .

#   'n' which tells after completing a task ==> how much time does it have to wait for the next same task to done .
# 
#   Here we will return the task which have the highest_frequecy first.
# 

#   Here after executing a task .. the task has to cooldown for some time ... after reducing its frequency value ==> here we use the queue
#       in the queue we store the freq,time value --> freq => which tells us that how times stills this same task to be done ... time tell's us the interval after completing the task.
# 
#    max_heap --> which effecively retrives the max_freq task to return 1st 
#   
#   Greedy --> algo --> clue-1: -> here we have the mini_time 
                  # --> clue-2: -> we repeatdely took the high_freq task and decrement(means reducing) and insert back to the heap
#                   --> clue-3: -> by decrementing the freq.... we reach to the solution 
# 
# Greedy --> here we are choosing the best(highest_freq_task) at every step -> to reach the mini_time to complete all task.

#  max_heap + greddy + queue 
def task_scheduler(tasks,n):
    
    from collections import Counter ,deque
    import heapq 
    
    freq = Counter(tasks)
    
    cooldown = deque()
    
    max_heap = []
    for char  in freq:
        heapq.heappush(max_heap,-freq[char])
    
    time = 0 
    while max_heap or cooldown:
        time += 1
        if max_heap:
            count = heapq.heappop(max_heap)
            
            count += 1 
            if count <0:
                cooldown.append((count,time+n))
                
        if cooldown and cooldown[0][1] == time:
            remaining_count_char_freq , next_availabe_time_to_execute_task =cooldown.popleft()
            
            heapq.heappush(max_heap,remaining_count_char_freq)
            
    return time 
    
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(task_scheduler(tasks,n))