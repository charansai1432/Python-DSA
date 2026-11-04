# here we aren't using the max_heap for this question 
#  even though in the question they mentioned the k_pairs_with_smallest ---> smallest we generally use the max_heap right 

#  but here we aren't using the max_heap for this question 


#  we are using the min_heap for this question ==> we want to repeatedly retrieve the pair with the smallest sum.
#   {VVVIMP} => A min_heap help's us to give the smallest sum first.

#  pattern recoginition 
                #  k pairs with smallest sums ==> min_heap

# #  Here 
# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3

# for this question first we will generate the pair for each row i.e for the [  (1,2),(1,4),(1,6)  ,   (7,2),(7,4),(7,6),   (11,2),(11,4),(11,6)  ]  this are the all pairs for the each row 
#  here we will store the 1st pair each row i.e [ (1,2) , (7,2) ,(11,2) ] in the heap 
#  
#  but in the heap we will store the [(total,i,0)] -- > while storing the 1st pair element in the heap 

#  (total,i,0) --> which tells us that ...===> i = nums1 index and 0 or j --> nums2 index 

#  when heap has elements and len of result is less than the k .. then we pop the elements in the heap 

#  after poping the elements we have to store it in the result ---> with actual value's.

#  after poping the elements ---> we have to insert the next pair from the same row .. (here same row is nothing but --> if we delete from the 1st element from nums1 then we have to insert nums1 index 0 element with the nums2 index 1 element we have to insert in to the heap)


import heapq

def k_pairs_with_smallest_sums(nums1, nums2, k):
     
    heap = []

        # Step 1: Insert the first pair from each row
    for i in range(min(len(nums1), k)):
        total = nums1[i] + nums2[0]
        heapq.heappush(heap, (total, i, 0))

    result = []

        # Step 2: Extract the K smallest pairs
    while heap and len(result) < k:

        total, i, j = heapq.heappop(heap)

        result.append([nums1[i], nums2[j]])

            # Step 3: Insert the next pair from the same row
        if j + 1 < len(nums2):

            next_total = nums1[i] + nums2[j + 1]

            heapq.heappush(
                heap,
                (next_total, i, j + 1)
            )

    return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(k_pairs_with_smallest_sums(nums1,nums2,k))



##### practising again to remember the logic 

def k_pairs_smallest_sums(nums1,nums2,k):
    
    import heapq 
    result = []
    heap = []
    for i in range(min(len(nums1),k)):
        
        total = nums1[i] + nums2[0]
        heapq.heappush(heap,(total,i,0))
        
    while heap and len(result) < k:
        total , i ,j = heapq.heappop(heap)
        result.append([nums1[i],nums2[j]])
        
        if j + 1 < len(nums2):
            new_total = nums1[i] + nums2[j+1]
            heapq.heappush(heap,(new_total,i,j+1))
    return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print(k_pairs_smallest_sums(nums1,nums2,k))
    
    
    
### practising again to remember the logic

def k_pairs_small_sum(nums1,nums2,k):
    result = []
    heap = []
    import heapq 
    for i in range(min(len(nums1),k)):
        total = nums1[i] + nums2[0]
        heapq.heappush(heap,(total,i,0))
    
    while heap and len(result) < k:
        total , i , j = heapq.heappop(heap)
        
        result.append([nums1[i],nums2[j]])
        
        if j + 1 < len(nums2):
            new_total = nums1[i] + nums2[j+1]
            heapq.heappush(heap,(new_total,i,j+1))
    return result 

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print(k_pairs_small_sum(nums1,nums2,k))