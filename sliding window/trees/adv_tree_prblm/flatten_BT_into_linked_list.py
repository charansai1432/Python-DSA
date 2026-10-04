class flatten_BT_into_linkedlist:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = flatten_BT_into_linkedlist(1)
root.left = flatten_BT_into_linkedlist(2)
root.left.left = flatten_BT_into_linkedlist(3)
root.left.right = flatten_BT_into_linkedlist(4)
root.right = flatten_BT_into_linkedlist(5)
root.right.right = flatten_BT_into_linkedlist(6)




# it is the iterative approach

def flatten_BT_to_LL(root):
    
    if root is None:
        return None
        
    while root:
        if root.left:
            right_subtree = root.right
            
            root.right = root.left 
            
            root.left = None
            
            right_most_node = root.right
            
            while right_most_node.right:
                right_most_node = right_most_node.right
                
            right_most_node.right = right_subtree
            
        root = root.right 
    return root
flatten_BT_to_LL(root)

# print flattened linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.right
    print("None")

print_linked_list(root)