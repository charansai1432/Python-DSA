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

# odd_even linked list 

def odd_even_LL(head):
    odd = head 
    even = head.next 
    even_head = even 
    while even is not None and even.next is not None:
        odd.next = even.next 
        odd = odd.next 
        
        even.next = odd.next 
        even = even.next 
        
    odd.next = even_head 
    return head 
head = odd_even_LL(head)

while head is not None:
    print(head.data,end="->")
    head = head.next 
print("None")