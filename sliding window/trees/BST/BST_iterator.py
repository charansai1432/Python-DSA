
class BST_iterator:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = BST_iterator(7)
root.left = BST_iterator(3)
root.right = BST_iterator(15)
root.left.left = BST_iterator(1)
root.left.right = BST_iterator(5)

root.right.left = BST_iterator(10)
root.right.right = BST_iterator(20)

def bst_iterator(root):
    stack = []
    def insert_left_elements(root):
        while root:
            stack.append(root)
            root = root.left
    insert_left_elements(root)
    
    def next(root):
        
        root = stack.pop()
        if root.right:
            insert_left_elements(root.right)
        return root.val
    
    def hasNext():
        return len(stack) > 0
    
    while hasNext():
        print(next(root))
bst_iterator(root)