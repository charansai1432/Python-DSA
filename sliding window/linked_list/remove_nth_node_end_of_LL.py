# remove_nth_node_end_of_LL

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


n = 2 # that means remove the 2nd last node from the {END} of an Linked List 

# remove the nth from a linked_list 
#   1. pattern recognition ==> whenever in the question they asked remove the nth node from the end THINK
            # - fast and slow pointer + dummy node 
            # - fast and slow pointer with gap + dummy node 

# we have to delete the nth node from the end of an linkedlist and return the answer
# here the GAP is provided by the for loop .


# Here the fast and slow pointer MOVE only {ONE STEP} at a time.
# 

# approach 
#1. create a dummy node 
#2. attach the dummy to head 
# point the fast and slow pointers to the dummy node
# 
# move the fast pointer only 'n' steps ==> why 'n' which gives the GAP to reach the target 
# while loop if fast is not None ==> move the slow and fast pointer's one at a time.

# {VVVIMP}==> whenever the fast pointer points to the none 
# the element next to the slow pointer is the nth node to remove 
# we can simple remove it using ==> slow.next = slow.next.next ==> removes the 'n' th node from the end of an linked_list.
# return dummy.next ==> which gives the original list of element by removing the dummy node ==> which we created 


# {VVVIMP} ==> The dummy node is a temporary extra node placed before the actual head to make deletion easier. 
#  Remember this simple rule
# A dummy node helps you delete the first node without writing separate deletion logic for the head.


def remove_nth_node_of_LL(head,n):
    dummy = Node(-1)
    dummy.next = head 
    fast = slow = dummy 
    
    for i in range(n):              
        fast = fast.next 
        
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next 
        
    slow.next = slow.next.next 
    return dummy.next 
head = remove_nth_node_of_LL(head,n)

while head is not None:
    print(head.data,end="->")
    head = head.next 
print("None")
    