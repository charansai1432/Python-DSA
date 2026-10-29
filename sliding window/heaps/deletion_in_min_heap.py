
# heap = [50, 30, 20, 15, 10, 8, 16]


# approach 
# the deletion of min_heap ==> means we have to delete the smallest element in the heap array 
# generally in the heap_array the 1st element is the smallest element --- how? ==> {in the question they asked about the min_heap} --> in the min_heap the parent has to small right 
# such that when we traverse the tree structure ==> the 1st element is stored in the list --> and for a given valid min_heap --> the 1st element is smallest element in the heap array ==> beccause in the min_heap parent is smallest right 

heap = [2, 5, 8, 10, 7, 15]

def deletion_in_min_heap(heap):
    
    if not heap:        # empty heap 
        return None 
    
    minimum = heap[0]       # assign the 1st element in the heap as minimum 
    
    last = heap.pop()           # pop the last element in the heap array 
    
    if heap:                                        # even after removing the element's in the heap array ==> if we still have many elements we process it 
        heap[0] = last 
        i = 0                       # starting and len which gives the position 
        n = len(heap)
        
        while True:                     # traverse all elements in the heap array.
            
            left_index = 2*i + 1                    # which gives the left_index & right index to the current element 
            right_index = 2*i + 2 
            
            smallest = i   #(cur_element)                         # intially we are assuming that this is our smallest element 
            
            # here the left or right_index should not exceed the n (because index values can't exceed the len of heap array right)
            
            # heap[smallest] ==> which gives the currnet_element
            
            if left_index < n and heap[left_index] < heap[smallest]:        # for our cur_element calculate the left_index and right_index and which index gives the smallest element we will take that  
                smallest = left_index                                       
                
            if right_index < n and heap[right_index] < heap[smallest]:
                smallest = right_index
                
            if smallest == i:               # smallest == i means the cur_element and index share same value we perform break --> means if left/right index == i(cur_element index ) i.e parent <= child break (because already valid min_heap)
                break 
            
            heap[i],heap[smallest] = heap[smallest],heap[i]         # if not valid min_heap ==> just swap the elements of cur_element with left/right index value element 
            
            i = smallest                                                    # i = smallest ===> smallest which gives the down side element right in simple smallest is left/right index value of cur_element right .. i.e down to cur_element 
                                                                # as in the question we have to move the down side we perform the i = smallest 
    return heap,minimum
print(deletion_in_min_heap(heap))               #([16, 30, 20, 15, 10, 8], 50)
            