class construct_BT_from_inorder_and_preorder:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def build_tree(preorder,inorder):   
    
    inorder_hashmap = {}
    
    
    for i in range(len(inorder)):
        inorder_hashmap[inorder[i]] = i 
        
    preorder_index = 0
    
    def build(left,right):
        
        nonlocal preorder_index
        if left  > right:
            return None
        
        root_value = preorder[preorder_index]
        
        preorder_index += 1
        
        root = construct_BT_from_inorder_and_preorder(root_value)
        
        root_index = inorder_hashmap[root_value]
        
        root.left = build(left,root_index - 1)
        
        root.right = build(root_index+ 1, right)
        
        return root
    return build(0,len(inorder) - 1)

        
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = build_tree(preorder,inorder)



def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)

tree = build_tree(preorder, inorder)
# inorder_traversal(tree)


###################### practising again to remember the logic ###################################

def build_tree(preorder,inorder):
    
    inorder_hashmap = {}
    
    for i in range(len(inorder)):
        inorder_hashmap[inorder[i]] =i
        
   
    preorder_index = 0
    def helper(preorder,inorder,left,right):
        
        nonlocal preorder_index
        
        if left > right:                # here the left and right are the index positions of the inorder list 
            return None
        
        root_value = preorder[preorder_index]
        root = construct_BT_from_inorder_and_preorder(root_value)
        
        preorder_index += 1
        
        root_value_index=inorder_hashmap[root_value]
        
        root.left = helper(preorder,inorder,left, root_value_index - 1)
        root.right = helper(preorder,inorder,root_value_index + 1, right)
        return root
    return helper(preorder,inorder,0,len(inorder) - 1)

    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = build_tree(preorder,inorder)

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)
inorder(root)


# here left and right if condition is used the base condition to stop the recrusion 

# and also here the left and right which provides the valid index ranges to build the tree 


# root_value_index ? => i.e the root value left side element is lessthan the root i.e root_value_index - 1 which gives the left side element for the root element 
# the same logic to get the right side elements of the root value ie root_value_index + 1

