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
# node = Node(10)
# head = node
# current = head 

    
    
# delete at end 

def delete_begin(head):
    
    if head is None:
        return None
    
    head = head.next 
    return head 
    
head = Node(10)


current = head 
arr =  [20,30,40,50]

for i in range(len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    current = current.next 

head = delete_begin(head)
current = head 
while current is not None:
    print(current.data,end = "->")
    current = current.next 
print("None")



# delete the node at end

def delete_end(head):
    
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    current = head 
    
    while current.next.next is not None:
        current = current.next
        
    current.next = None
    
    return head 

head = Node(10)


current = head 
arr =  [20,30,40,50]

for i in range(len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    current = current.next 
 
head = delete_end(head)
current  = head 

while current is not None:
    print(current.data,end="->")
    current = current.next
print("None")


# delete a node after  a target 

def delete_node_target(head,target):
    
    if head is None:
        return None
    
    if head.data == target:
        return head.next
    
    current = head 
    
    if current.next is None:
        return head 
    while current.next is not None and current.next.data != target:
        current = current.next 
        
    if current.next is None:
        return head 
    
    current.next = current.next.next 
    return head 
head = Node(10)



current = head 
arr =  [20,30,40,50]

for i in range(len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    current = current.next 
 
 
head = delete_node_target(head,30)

current = head 
while current is not None:
    print(current.data,end="->")
    current = current.next 
print("None")


