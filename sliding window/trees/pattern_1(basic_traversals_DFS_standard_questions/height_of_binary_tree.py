

# optimal solution 

class Treenode:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
        
def height(root):
    if root is None:
        return 0 
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left,right)


root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left =Treenode(4)
root.left.right = Treenode(5)
print(height(root))


# here we are returning the 1 + max(left,right) => so here we use along with the print(function_name)
# in the basic operations of tree program we are not doing the print(function_name) due to we aren't returning anything 
# we are just printing the cur_root at the traversal okk 

# so for the printing NO need for the print(function_name)  => just function_call is enough 


