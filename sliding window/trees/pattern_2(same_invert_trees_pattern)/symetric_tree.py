

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def issymmetric(root):
    if root is None:
        return True   
    def symmetric_tree(left,right):
        
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        left_side = symmetric_tree(left.left,right.right)
        right_side = symmetric_tree(left.right,right.left)
        return left_side and right_side
    return symmetric_tree(root.left,root.right)
# 
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(2)

root.left.left = Treenode(3)
root.left.right = Treenode(4)

root.right.left = Treenode(4)
root.right.right = Treenode(3)

print(issymmetric(root))
# print(symmetric_tree(root))