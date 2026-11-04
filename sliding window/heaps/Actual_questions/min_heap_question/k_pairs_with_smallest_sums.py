# here we aren't using the max_heap for this question 
#  even though in the question they mentioned the k_pairs_with_smallest ---> smallest we generally use the max_heap right 

#  but here we aren't using the max_heap for this question 


#  we are using the min_heap for this question ==> we want to repeatedly retrieve the pair with the smallest sum.
#   {VVVIMP} => A min_heap help's us to give the smallest sum first.


#  pattern recoginition 
                #  k pairs with smallest sums ==> min_heap

import heapq
def k_pairs_with_smallest_sums(nums1, nums2, k):
    pass 
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