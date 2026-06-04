
# brute force approach 

def painter_partition(boards,painters):
    l = max(boards)
    r = sum(boards)
    for min_work in range(l,r+1):
        cur_painters = 1
        cur_work = 0 
        for board in boards:
            if cur_work + board > min_work:
                cur_painters += 1
                cur_work = board
            else:
                cur_work += board
        if cur_painters <= painters:
            return min_work
print(painter_partition([10,20,30,40],2))       #60





# {VVVIMP} ==> here we are finding minimum_work can be assigned to a painter such that no painter can feel the burden of work 
# Minimize the workload of the busiest painter.

# Goal

# Minimize the maximum work assigned to any painter.

# optimal solution approach 

# mid = answer = max_work_per_painter 

# {VVVIMP}  below one 

# interviewer gives:

# maximum_work = 60

# Ask:

# If one painter can paint at most 60 units, how many painters do I need?

# This is exactly what feasibility finds.

def painter_partition(boards,painters):
    pass
    def possible(max_work_per_painter):
        
        painters_needed= 1
        cur_work = 0
        for board in boards:
            if cur_work + board > max_work_per_painter:
                painters_needed += 1
                cur_work = board
            else:
                cur_work += board
        # print(painters_needed)
        return painters_needed <= painters
  
    l = max(boards)
    r = sum(boards)
    answer = r
    while l <= r:
        mid = l + (r-l)//2
        if possible(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer


print(painter_partition([10,20,30,40],2))


# Interview One-Line Summary

# For Painter's Partition:

# We binary search the maximum work a painter is allowed to do.
# For each candidate value (mid), we greedily assign continuous boards and count how many painters are needed. 
# If the required painters are less than or equal to the available painters, the workload limit is feasible. We then try to minimize it.