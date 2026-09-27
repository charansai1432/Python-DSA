
class recover_BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = recover_BST(3)
root.left = recover_BST(1)
root.right = recover_BST(4)
root.right.left = recover_BST(2)

def recov_BST(root):
    if root is None:
        return None
    first = None
    second = None
    previous = None
    def dfs(root):
        if root is None:
            return None
        nonlocal first,second,previous
        
        dfs(root.left)
        
        if previous is not None:
            
            if previous.val > root.val:
                if first is None:
                    first = previous
                second = root
        previous = root
        
        dfs(root.right)
        
    dfs(root)
    first.val , second.val = second.val,first.val
    return root
root = recov_BST(root)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
inorder(root)
        