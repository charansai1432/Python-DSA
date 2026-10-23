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

# def reorder_LL(head):
#     fast = slow = head 
#     while fast is not None and fast.next is not None and fast.next.next is not None:
#         slow = slow.next 
#         fast = fast.next.next 
        
#     second = slow.next 
#     slow.next = None 
    
#     previous = None 
#     current = second 
    
#     while current is not None:
#         next_node = current.next  
#         current.next = previous
#         previous = current 
#         current = next_node
        
#     first = head 
#     second = previous 
    
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
        
    