
class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = Treenode(5)
root.left = Treenode(3)
root.left.left = Treenode(2)

root.left.right = Treenode(4)
root.right = Treenode(6)
root.right.right = Treenode(7)

def delete_BST(root,key):
    if root is None:
        return None
    if key < root.val:
        root.left = delete_BST(root.left,key)
    elif key > root.val:
        root.right = delete_BST(root.right,key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        successor = root.right
        while successor.left is not None:
            successor = successor.left
            
        root.val = successor.val
        root.right = delete_BST(root.right,successor.val)
    return root
root = delete_BST(root,3)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.val,end = " ")
    inorder(root.right)
inorder(root)                   # 2 4 5 6 7 

