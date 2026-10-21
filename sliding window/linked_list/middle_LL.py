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



# middle element of an linkedlist 
#approach is using the fast and slow pointers 
# intially the fast and slow pointers are at head 
# here fast pointer moves two times at once 
# slow pointer moves only 1 step at a time 
# and the middle element is always find in the slow pointer 

# middle element = when the fast pointer reaches {none} at that time slow pointer is at middle 


#{VVVIMP} => here fast is read pointer 
# slow is a write pointer 

# fast is not None and fast.next is not None: => here fast is not none means we have one 
# fast.next is not none => means we have the 2nd node too 
# then only we can implement the fast and slow pointer ===> {VVVIMP} ==> we must have the atleast(>=) two nodes to implement the fast and slow pointer's

def middle_LL(head):
    slow = fast = head 
    while fast is not None and fast.next is not None:       # here in the while condition we use only fast is not none beacuse => fast is a read pointer and this pointer has to tell when we reach the none that's why we used the inside the while loop like fast is not none and fast.next is not none.
        slow = slow.next 
        fast = fast.next.next 
    return slow 
answer = middle_LL(head)
print(answer.data)