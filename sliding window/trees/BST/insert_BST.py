
# Pattern : BST Search + Modify
#
# Idea:
# 1. Compare the value with current node.
# 2. If value is smaller -> Go Left.
# 3. If value is greater -> Go Right.
# 4. When we reach None -> Create the new node.
# 5. Return the updated root.

# 🧠 Memory Sentence

# Don't memorize this line:

# root.left = insert(root.left, val)

# Instead, remember why it exists:

# "The child returns an updated subtree, and the parent reconnects that updated subtree to its left (or right) child."


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -------------------------
# Tree Creation
# -------------------------

root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(14)

root.right.right.left = TreeNode(13)


def insert_BST(root,val):
    
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_BST(root.left,val)
    elif val > root.val:
        root.right = insert_BST(root.right,val)
    return root 
answer = insert_BST(root,5)
# answer = insert_BST(root, 5)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

inorder(answer)


# Pattern
# BST Search + Modify


# Here the current node compares the value with itself.
# If the value is smaller,
# go to the left subtree.
#
# If the value is greater,
# go to the right subtree.


# When we first reach None,
# that is the correct position to insert the new node.

# Base Case
if root is None:
    return TreeNode(val)


# Very Important

# Why root.left = insert(...) ?

# The recursive function returns the updated left subtree.

# The parent reconnects that updated subtree
# to its left child.

# Same for the right subtree.


# Finally

# Return the updated subtree root
# so that the parent can reconnect it.

# This pattern is used in:
# Insert BST
# Delete BST
# AVL Trees
# Red Black Trees
# Construct Binary Tree

                                 