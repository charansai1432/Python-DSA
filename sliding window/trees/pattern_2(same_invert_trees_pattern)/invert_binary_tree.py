

# Pattern Recognition

# If interviewer says:

# Mirror tree
# Reverse tree
# Flip tree
# Invert tree

# Think:

# Current node action

# +

# Recurse children


# optimal solution 


class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def invert_tree(root):
    
    if root is None:
        return None
    
    root.left,root.right = root.right,root.left
    invert_tree(root.left)
    invert_tree(root.right)
    # left_side_invert = invert_tree(root.left)
    # right_side_invert = invert_tree(root.right)
    return root

# Helper function to print the tree so we can see it
def preorder(root):
    if root is None:
        return 
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
preorder(root)
print()
preorder(invert_tree(root))
print()


# invert_tree rearranges the tree, but it doesn't display it. 
# When you run invert_tree(root), the function does all the hard work of swapping the left and right branches. 
# When it finishes, it hands you back the top node (the root).

# Here is why you can't just print that root directly:

#####################################################{VVVIMP => LEARN THIS BEFORE DOING THE QUESTION }##################################################################


# preorder is walking through the house:
# To actually see the work the movers did, you have to use the key to open the door, walk into the first room, write down what's there, walk into the next room, and so on. 
# The preorder function is the step-by-step process of walking through the house to show you the furniture.