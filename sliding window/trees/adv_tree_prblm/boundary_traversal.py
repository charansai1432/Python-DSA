class boundary_traversal:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = boundary_traversal(1)
root.left = boundary_traversal(2)
root.right = boundary_traversal(3)
root.left.left = boundary_traversal(4)
root.left.right = boundary_traversal(5)
root.left.right.left = boundary_traversal(7)
root.left.right.right = boundary_traversal(8)
root.right.right = boundary_traversal(6)

def boundary__traversal(root):
    if root is None:
        return []
    
    result = []
    
    
    # leaf node check 
    def is_leaf(root):
        return root.left is None and root.right is None
    
    if not is_leaf(root):
        result.append(root.val)
        
    # left_boundary 
    node  = root.left
    while node :
        if not is_leaf(node):               # in every iteration we have to check whether the current node is leaf or not. => if leaf we want append that value in the add_leaves function only 
                                            # like in the boundary traversal first we have to add the left boundary after that only we have to add the leaf nodes and then right boundary 
                                                # for that reason only we are not adding the leaf nodes at starting okk {{VVIMP}}
            result.append(node.val)
            
        if node.left:
            node  = node.left
        else:
            node = node.right
        
        
    # add all leaf nodes
    
    def add_all_leaf_nodes(node):
        
        if node is None:
            return 
        
        if is_leaf(node):
            result.append(node.val)
            return 
        
        add_all_leaf_nodes(node.left)
        add_all_leaf_nodes(node.right)
    add_all_leaf_nodes(root)
    
    
    # right boundary 
    
    right_boundary = []
    
    node = root.right
    while node:
        
        if not is_leaf(node):
            right_boundary.append(node.val)
        
        if node.right:
            node = node.right
        else:
            node = node.left
            
    right_boundary.reverse()
    result.extend(right_boundary)
    
    return result
print(boundary__traversal(root))


################################ practising again to remember #############################

def boundary_traversall(root):
    
    if root is None:        # base condition => if no tree is there ==> return the empty list.
        return []
    
    
    result = []
            
    def is_leaf(root):
        return root.left is None and root.right is None
    
    if not is_leaf(root):
                result.append(root.val)
                
    
    
    # left boundary 
    node = root.left
    while node:
        if not is_leaf(node):
            result.append(node.val)
            
        if node.left:
            node = node.left
        else:
            node = node.right
            
    # add all leaf nodes in to the result list 
    
    def add_all_leaf_nodes(node):
        if node is None:
            return 
        
        if is_leaf(node):
            result.append(node.val)
            
        add_all_leaf_nodes(node.left)
        add_all_leaf_nodes(node.right)
    add_all_leaf_nodes(root)
    
    
    # right boundary 
    right_bounddary = []
    node = root.right 
    while node:
        if not is_leaf(node):
            right_bounddary.append(node.val)
        if node.right:
            node = node.right
        else:
            node = node.left
    right_bounddary.reverse()
    result.extend(right_bounddary)
    
    return result
    
    
    
print(boundary_traversall(root))
################################ practising again to remember #############################
def boundary(root):
    if root is None:
        return []
    
    result = []
    
    def is_leaf(root):
        return root.left is None and root.right is None
    
    if not is_leaf(root):
        result.append(root.val)
        
    # left boundary 
    node = root.left 
    while node:
        
        if not is_leaf(node):
            result.append(node.val)
        
        if node.left:
            node = node.left
        else:
            node = node.right 
    
    
    # this function help us to traverse the entire tree to find the leaf nodes in a tree => so for that only we are doing the add_all_leaf_nodes(root.left/right)
    def add_all_leaf(root):
        if root is None:
            return 
        if is_leaf(root):
            result.append(root.val)
        add_all_leaf(root.left)                     # goal of add_all_leaf is to visit every node in the tree and collect all the leaf nodes (nodes with no children). 
                                                        #To do that, we need to {{VVIMP}  TRAVERSE  the entire tree}.
        add_all_leaf(root.right)
    add_all_leaf(root)
    
    
    # right bounday 
    
    right_side = []
    
    node = root.right 
    while node:
        if not is_leaf(node):
            right_side.append(node.val)
        if node.right:
            node = node.right 
        else:
            node = node.left 
            
    right_side.reverse()
    result.extend(right_side)
    return result     
print(boundary(root))




        
        