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



# reverse a  linked list from the original linked list i,e 10-20-30-40-50-none to 50-40-30-20-10-noe 


# here we will solve this reverse linked list question using the 3 pointers (previous,current,next_node)

# previous which points to the previous 
# cur_node = processing cur_node 
# next_node = which saves the next node to current 

# approach the question => 1. 1st we will sae the next_node to current 
# 2. we will remove the link of cur_node and attach the previous node to cur_node  (reversal happens here )

# 3. we will move the previous pointer to cur_node  
# 4. and then we will move the cur_node to next_node (as current node reversal is done na so we will move to the next node ).
# 5. at last the previous pointer points to the last node okk .. and we havve to print that last pointer ok i.e return previous 

# ==> In traditional we will return the head right ==> here we return the previous because the cur_node.next is none and at that time previous points to cur_node i.e previous points to cur_node i.e pointer is at last node means previous so we return the return previous.

def reverse_list(head):
    previous = None
    current = head 
    while current is not None:
        next_node = current.next 
        current.next = previous 
        previous = current 
        current = next_node
    return previous
 
head = reverse_list(head)

current = head 

while current is not None:
    print(current.data,end = "->")
    current = current.next 
print("None")

