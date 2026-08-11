class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def search_BST(root,target):
    if root is None:
        return None
    
    if root.val == target:
        print("searching on root",root.val)
        return root   # return the node itself
    
    if target < root.val:
        print("Searching left:", root.val)
        return search_BST(root.left,target)
    else:
        print("searching right:",root.val)
        return search_BST(root.right,target)

# Example BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

answer = search_BST(root,3)
print("founded the target:",answer.val)
# if answer:
#     print("Found:", answer.val)   # Output: Found: 3
# else:
#     print("Not found")
