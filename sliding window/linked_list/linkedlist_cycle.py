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

# you need to set the next pointer of the last node (or any downstream node) to point back to an earlier node in the list rather than None.

## the linked list cycle ===> we have to find out the linked list has any cycle or not 
#
 # A cycle is nothing but a node points to some another other node in a linked list then we have to cycle 
#
# linked list cycle 
def linked_list_cycle(head):
    fast = slow = head 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        
        if slow is fast:
            return True 
    return False 
print(linked_list_cycle(head))