


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