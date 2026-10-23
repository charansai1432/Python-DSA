class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Shared part (intersection)
intersect = ListNode(8)
intersect.next = ListNode(10)

# First linked list: 3 -> 7 -> 8 -> 10
headA = ListNode(3)
headA.next = ListNode(7)
headA.next.next = intersect

# Second linked list: 99 -> 1 -> 8 -> 10
headB = ListNode(99)
headB.next = ListNode(1)
headB.next.next = intersect

# Function to print a list
def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")

print("List A:")
print_list(headA)

print("List B:")
print_list(headB)


## intersection of two LL

def intersection_of_two_LL(headA,headB):
    a = headA
    b = headB 
    while a is not b:
        if a is None:
            a = headB 
        else:
            a = a.next 
        if b is None:
            b = headA 
        else:
            b = b.next 
    print("\n")
    print("print the intersecting node")
    return a.val  # return b both are same due to both share the common intersecting node right 

print(intersection_of_two_LL(headA,headB))