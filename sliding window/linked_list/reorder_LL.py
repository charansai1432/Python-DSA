class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

arr = [20,30,40,50]

head = Node(10)
current = head 
for i in range(len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    current = current.next 
    
current = head 

print("printing the current linkedlist ")
while current is not None:
    print(current.data,end="->")
    current = current.next 
print("None")


# ## reorder_LL
# approach 
# 
# question is { attach the 1st node to last node and 2nd node to last 2nd node and so no. }
#
# middle + divide the LL at middle position (slow) + reverse the second 2nd half + and perform the merge Operation 
# 
# {VVVIMP} ==> Pattern recognition
# 
#   - when in a question they asked some thing like attach the 1st node to last node and 2nd node to last 2nd node and so no 
#       - immediatley think it is a middle  + divide the LL at middle position (slow) + reverse the second 2nd half + and perform the merge Operation 
#               -- this is the pattern 
# 
# 

# def reorder_LL(head):
        # finding the middle element 
#     fast = slow = head 
#     while fast is not None and fast.next is not None and fast.next.next is not None:
#         slow = slow.next 
#         fast = fast.next.next 
        
        # split at the middle postion 
#     second = slow.next                    # creates the 2nd LL
#     slow.next = None                          # make sure that the 1st LL has to set None and slow postion ==> this 2 lines helps us to create a two LL
    
    
    # reverse the 2nd half 
    
#     previous = None 
#     current = second 
    
#     while current is not None:
#         next_node = current.next  
#         current.next = previous
#         previous = current 
#         current = next_node
        
        
        # mark the position of the head in the both 1st and 2nd LL
        
#     first = head 
#     second = previous 
    
    
    # Merge logic for the LL of the 1st node to 1st last node alternateviley at every iteration 
#     while second is not None:
#         first_next_node = first.next 
#         second_next_node = second.next 
        
#         first.next = second 
#         second.next = first_next_node
        
#         first = first_next_node
#         second = second_next_node
    
#     return head 

# head = reorder_LL(head)

# while head is not None:
#     print(head.data,end="->")
#     head = head.next 
# print("None")





######### practisng again to remember###################3


def reorder_L(head):
    fast = slow = head 
    
    while fast is not None and fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

        
    # second = slow.next   
    # slow.nxt = None

    second = slow.next 
    slow.next = None
    
    previous = None 
    current = second 
    while current is not None:
        next_node = current.next 
        current.next = previous
        previous = current 
        current = next_node
        
    first = head 
    second = previous 
    
    while second is not None:
        first_next_node = first.next 
        second_next_node = second.next 
        first.next = second 
        second.next = first_next_node
        
        first = first_next_node
        second = second_next_node
    
    return head
        
head = reorder_L(head)

while head is not None:
    print(head.data,end="->")
    head = head.next 
print("None")
        
    