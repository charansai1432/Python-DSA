# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # value of the node
        self.next = next    # pointer to the next node



# Number 342 represented as 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Number 465 represented as 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

#  same as additino in the general math 
#  we will add the element from the end of LL's 
# and also we will return the answer from the end of result LL
# {VVVIMP} refer the {notes} which i wrote the logic 


# {VVVVVIMP} ==> if two linkedlists are given ==> and the final LL is in a single line format 
#  then we have to use the dummy node ==> dummy node which helps main tain order 

## add two numbers in a linked list 

def add_two_numbers(l1,l2):
    dummy = ListNode(-1)
    current = dummy 
    carry = 0 
    while l1 is not None or l2 is not None or carry != 0:
        
        total = 0
        if carry != 0 :
            total += carry 
            
        if l1:
            total += l1.val 
            l1 =  l1.next 
        if l2:
            total += l2.val  
            l2 = l2.next
            
        digit = total % 10 
        carry = total // 10 
        
        digit = ListNode(digit)
        
        current.next = digit   
        current = current.next
    return dummy.next  
head = add_two_numbers(l1,l2)
    
while head is not None :
    print(head.val,end="->")
    head = head.next  
print("None")
