def k_closest_points_origin(points,k):
    import heapq
    heap = []
    result = []
    for x,y in points:
        distance = x*x+y*y 
        heapq.heappush(heap,(-distance,x,y))
        if len(heap) > k :
            heapq.heappop(heap)
    while heap:
        distance,x,y = heapq.heappop(heap)
        result.append([x,y])
    return result 
print(k_closest_points_origin([[1,3],[-2,2]],1))        # [[-2,2]]
            