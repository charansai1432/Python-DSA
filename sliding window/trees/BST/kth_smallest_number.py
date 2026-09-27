
#       kth smallest number in a BST tree => if k = 1 

#   here 'k' which determines the kth smallest number in a arr/tree.
#       i.e if k == 2 i.e we have to find the 2nd smallest number in an tree
# 
#   i.e if the arr is sorted => then we can simple find out the smalllest element in the left side of an array 
# 
#          the smallest element definately find out the left side of an BST.
                # then we dont need to find that one on the right side of an BST.
                
#  for example if => [1,2,3,4,5,6] and k = 2 ,3
#  i.e we have find the 2nd smallest number in array => as array is sorted the 2nd smallest element find in the left_side right 
# i.e here answer is 2 and for k = 3 is 3
# 

#  example => [5,6,7,8] and k = 2 , 3 
#  answer is 6, 7
# =================================================================================
#  pattern recognition 

# what is the interviewer asking for return => node 
# what is recrusion is returning => int 
# the travarsal order is Inoder travarsal (for this question )  => (left -> root -> right )
# the pattern is count pattern 


# This is a New Recursion Pattern for You

# You've already learned:

# DFS → child returns information → parent uses it

# Here:

# DFS
#  ↓
# Left subtree searches for kth element
#  ↓
# If found → return answer upward
#  ↓
# Otherwise process current node
#  ↓
# Then search right

# So the pattern is:

# Inorder + Count + Early Return

# Remember this name.

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = Treenode(5)
root.left = Treenode(3)
root.right = Treenode(7)
root.left.left = Treenode(1)
root.left.right = Treenode(4)



#  optimal solution approach 

def kth_smallest_number(root,k):
    count = 0
    def inorder(root,k):
        nonlocal count
        if root is None:
            return 
    
        left = inorder(root.left,k)
        if left is not None:
            return left
        count += 1
        if count == k:
            return root.val
        right = inorder(root.right,k)
    inorder(root,k)

print(kth_smallest_number(root,2))
# print(answer)
    
    
    
# brute force approach 


def kth_smallest_number(root,k):
    
    arr = []
    def inorder(root):
        if root is None:
            return 
        inorder(root.left)
        arr.append(root.val)
        inorder(root.right)
    inorder(root)
    
    arr.sort()
    return arr[k-1]
    
    
print(kth_smallest_number(root,2))
    