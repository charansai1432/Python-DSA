class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2

# node2.next = node3


# which creates a linnked list with values 10-20-30-40-50
node = Node(10)
head = node
current = head 

arr =  [20,30,40,50]

for i in range(1,len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    current = current.next 
    
    
## traverse a linked list 

# head = node
# current = head 
# while current.next is not  None:
#     print(current.data)
#     current = current.next 
    
    
## insertion at beginning of a linked_list

def insert_begin(head,val):
    
    new_node = Node(val)
    new_node.next = head 
    head = new_node
 
insert_begin(10,5)




## insertion at end of linkedlist

def insertion_end(head,val):
    
    # if linked_list is empty we will create a node with the val 
    if head is None:
        return Node(val)
    
    
    current = head 
    
    new_node = Node(val)
    
    # traversing linked_list until we find the None(last_node/tail node)
    
    while current.next is not None:
        current = current.next 
        
    current.next = new_node
    
    # finally returning the head 
    return head 
    
insertion_end(head, 80)





# insertion of after a node in linkedlist

def insertion_after_node(head,target,val):
    
    current = head 
    
    new_node = Node(val)
    
    if current is None:
        return head 
    
    while current.next is not None and current.data != target:
       current = current.next 
       
    new_node.next = current.next 
    
    current.next = new_node
        
    return head 
insertion_after_node(head, 20, 25)


def print_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

# Original linked list
head = Node(10)
current = head

for val in [20, 30, 40, 50]:
    current.next = Node(val)
    current = current.next

print_list(head)

# Insert at beginning
head = insert_begin(head, 5)
print_list(head)

# Insert at end
head = insertion_end(head, 80)
print_list(head)

# Insert after target 20
head = insertion_after_node(head, 20, 25)
print_list(head)