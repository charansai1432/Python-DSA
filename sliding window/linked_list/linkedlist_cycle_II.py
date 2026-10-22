class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        

head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

fifth.next = third      # cycle starts at 30



# print the node where cycle is started 

def cycle_LL_II(head):
    
    fast = slow = head 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        if slow is fast:
            slow = head 
            while fast is not slow:
                slow = slow.next 
                fast = fast.next 
            return slow   # we can also return the fast also because here we are finding the node where the both fast and slow pointer make an cycle i.e cycle starts 
    return None                 # if cycle exists just return the None
answer = cycle_LL_II(head)
print(answer.data)