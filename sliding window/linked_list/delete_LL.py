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


# delete a node that maatch the given the target 

def delete_node_target(head,target):
    
    if head is None:                    # empty linked list 
        return None
    
    if head.data == target:         # if the cur_head has the target value we have to print the next elements right so return head.next 
        return head.next
    
    current = head              # 1st node in a linked list 
    
    
    while current.next is not None and current.next.data != target:     # for example we have the elements 10-20-30-40-50 here => we have to delete the target node 
                                        # current.next is not none => i.e we can proceed further and that current.next.val is not equal to target -> then we have to move the head pointer forward.
        current = current.next 
        
    if current.next is None:                # means if given target node is not found in the linked list => we return the head 
        return head                 # example 10-20-30 and target is 40 ====> after all the traversing we will reach to the node 30 and here our target is 40 which isn't there in the linked_list 
                                            # here we have to write this if-condition {VVIMP - only after the while loop } ==> that helps us to know the target is not found and traversing in the entire linked_list (by while loop )
    
    current.next = current.next.next        # actuall deletion logic 
    
    return head             # return the head 
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


