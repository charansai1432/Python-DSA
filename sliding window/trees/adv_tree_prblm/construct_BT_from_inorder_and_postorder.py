class construct_BT_from_inorder_and_postorder:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def build_tree(inorder,postorder):
    
    post_order_index = len(postorder) - 1
    
    inorder_hashmap = {}
    
    for i in range(len(inorder)):
        inorder_hashmap[inorder[i]] =  i
        
    def helper(inorder,postorder,left,right):
        
        nonlocal post_order_index
        if left > right:
            return None
        
        root_value = postorder[post_order_index]
        
        root = construct_BT_from_inorder_and_postorder(root_value)
        post_order_index -= 1
        
        root_value_index = inorder_hashmap[root_value]
        
        root.right = helper(inorder,postorder,root_value_index + 1,right)
        root.left = helper(inorder,postorder,left,root_value_index - 1)
        return root
    return helper(inorder,postorder,0,len(inorder)-1 )
    
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = build_tree(inorder,postorder)


def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
inorder(root)