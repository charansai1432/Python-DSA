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

# the odd even Linked List 

########################################################################################

#   {question is } => we have arrange all the odd nodes to head and even nodes to next of odd nodes okkk
#       pattern is 
#               -   pointer wiring + maintain chain (individually).

# pos 1  2  3  4 5                  {VVIMP} => MAKE sure that postion always start from the {1} okk 
#    10-20-30-40-50-none

#  this position => pointer wiring 
        # - maintain chain  =>  here we maintain the two differnt chains right 
                    #  1. odd chain 
                    #  2. even chain 
    
    
########################################################################################                
# pattern recognition 

#  1. when in the question they asked about the         {rearrange odd,even nodes or maintaining their order, etc} .. 

#  like that is there in the question then we can assume it as the {POINTER WIRING + MAINTAINING CHAIN}
########################################################################################
    
#  approach 
#  1. point head to odd 
#  2. head next node point to the even node 
# 3. make sure that here we are attaching the all the even node chain back to odd chain 
#  4. so we have make sure , even_head = even do like this because the even chain also have the head right for that we have make it like this 
#  5. here even pointer is always forward to the odd pointer 
#  6. so we move the even pointer {FIRST}
#  7. now we have to attach the 1st odd node(head) to the even next node ok {VVIMP}
# 8. and move the odd pointer forward 
#  9. follow the same pointer to the even chain same as above one okk 
# 10. at last return the head ok 

    ########################################################################################

# odd_even linked list 

def odd_even_LL(head):
    if head is None:        # if linked list is empty => then we cannot make the odd and even position to the result list ==> so simple return the None
        return None 
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