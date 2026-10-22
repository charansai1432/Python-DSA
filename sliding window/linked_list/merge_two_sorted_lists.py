class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# List 1: 1 -> 2 -> 4
head1 = Node(1)
second1 = Node(2)
third1 = Node(4)

head1.next = second1
second1.next = third1


# List 2: 1 -> 3 -> 4
head2 = Node(1)
second2 = Node(3)
third2 = Node(4)

head2.next = second2
second2.next = third2



# {vvimp} = > actual question is we have to merge the two lists in a sorted manner.
# 
# 
# pattern Dummy + tail pointer 

# 1.  1st we create a dummy node and attach to the tail node 
# 2. every time we check in the two list's which value list has the small value we will attach into the tail node



def merge_two_sorted_list(head1,head2):
    
    dummy = Node(-1)
    tail = dummy 
    while head1 is not None and head2 is not None:
        
        if head1.data <= head2.data:            # this condition tells us that list1 is smallest for this iteration # checks which list has the smallest node and attach to tail node 
            tail.next = head1  
            head1 = head1.next          # after attaching to the tail node we have to move the tail pointer forward because for the next node we attach right either from list1 or list2 for that we have to move the tail pointer forward.
        
        else:
            tail.next  = head2          # 2nd list has the small value in this iteration 
            head2 = head2.next  
            
        tail = tail.next        # every time we have to move the tail pointer to attach for the next node 
        
    if head1 is not None:      # this line mainly tells us that the 1st list we have reached to end (at some time ) then we simple have to attach the list2 nodes with the tail node          # this means that either list1 or list2 for (list2 condition could if list2 is not None(some code logic )else:tail.next = list1)
        tail.next = head1 
    
    else:
        tail.next = head2 
        
    return dummy.next                   # dummy is a node we took because to attach all the nodes from list1 and list2 in a sorted manner ... and here return dummy.next which gives only the nodes which asked in the question to print in a sorted manner.

head  = merge_two_sorted_list(head1,head2)

while head is not None:
    print(head.data,end="->")
    head = head.next 
print("None")

