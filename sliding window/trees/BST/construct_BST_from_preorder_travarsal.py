
class construct_BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def build_BST_from_preorder(preorder,index,min_val,max_val):
    
    if index[0] == len(preorder):return None
    
    value = preorder[index[0]]
    
    if value <= min_val or value >= max_val:
        return None
    
    root = construct_BST(value)
    
    index[0] += 1
    
    root.left = build_BST_from_preorder(preorder,index,min_val,value)
    root.right = build_BST_from_preorder(preorder,index,value,max_val)
    
    return root
    
    
    
preorder = [8,5,1,7,10,12]
index = [0]    
root = build_BST_from_preorder(preorder,index,float('-inf'),float('inf'))

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.val , end=" ")
    inorder(root.right)
inorder(root)