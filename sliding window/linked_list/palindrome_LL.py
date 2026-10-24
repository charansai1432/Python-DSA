
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

arr = [2,2]

head = Node(1)
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


# palindrome linked list 
# palindrome means if we read the LL from the starting and ending it has to be same then its a palindrome other wise False

# approach 
# middle + divide the LL at middle position (slow) + reverse the second 2nd half + and comparing the two half values with each together 
#  
def palindrome_LL(head):
    
    if head is None:            # edge case 
        return True 
    
    fast = slow = head 
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next  
        fast = fast.next.next 
        
    second = slow.next  
    slow.next = None 
    
    current = second
     
    previous = None 
    
    while current is not None:
        next_node = current.next 
        current.next = previous 
        previous = current 
        current = next_node 
        
    second = previous 
    first = head 
    while second is not None:
        if first.data != second.data:
            return False 
        first = first.next  
        second = second.next 
    return True 
print(palindrome_LL(head))