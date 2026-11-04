def kth_smallest_element_in_sorted_matrix(matrix,k):
    import heapq 
    heap = []
    for row in matrix:
        for num in row:
            heapq.heappush(heap,-num)
            if len(heap) > k:
                heapq.heappop(heap)
    return -heap[0]
print(kth_smallest_element_in_sorted_matrix(
    [
        [1,5,9],
     [10,11,13],
     [12,13,15]
     ],
    8
))                  # 13 

