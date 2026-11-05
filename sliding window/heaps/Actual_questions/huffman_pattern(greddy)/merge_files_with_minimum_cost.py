
# brute force approach 

files = [5, 2, 4, 7]
files = [3, 8, 2, 6]

def merge_files_with_mini_cost(files):
    min_cost = 0 
    while len(files) > 1:
        first_small_file_size = min(files)
        files.remove(first_small_file_size)
        
        second_small_file_size = min(files)
        files.remove(second_small_file_size)
        
        min_cost += first_small_file_size + second_small_file_size
        
        new_file_size = first_small_file_size+ second_small_file_size

        files.append(new_file_size)
    return min_cost
print(merge_files_with_mini_cost(files))



files = [5, 2, 4, 7]
files = [3, 8, 2, 6]
# optimal solution 
def merge_files_with_minimum_cost(files):
    import heapq 
    min_cost = 0
    heapq.heapify(files)
    while len(files) > 1:
        first_small_sizefile = heapq.heappop(files)
        second_small_size_file = heapq.heappop(files)
        
        new_file_size = first_small_sizefile + second_small_size_file
        
        min_cost += first_small_sizefile + second_small_size_file
        
        heapq.heappush(files,new_file_size)
    return min_cost
print(merge_files_with_minimum_cost(files))