

# Lowest common ancestor means ==> questions which tells us that ==> we have to return the ancestor of the given nodes
# 
# for example if the inputs are node 4 node 5 their root is the ancestor common (lowest)
# 
# here to find the lowest common ancestor =>> if the cur_node has the left and right child 
# if that left and right child equals to the inputs we passed then it's cur_node is the ancestor 
# 
# that mean's if if left and right child's next node's is none => that means we reach the end of the nodes(leaf nodes)
# if that time if the left and right child is matched with the given input values then cur_node is the lowest common ancestor of the given inputs (LCA)

# optimal solution 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def lowest_common_ancestor(root,p, q):
    
    # base case
    if root is None or root == p or root == q:      # if tree is empty return the cur_node and if cur_node matches with the neither p or q return the cur_node to it's parent ... it doesn't means if the LCA  
        return root
    
    left = lowest_common_ancestor(root.left,p,q)
    right = lowest_common_ancestor(root.right,p,q)
    
    if left and right:          # this means the both p and q are found and cur_node is LCA
        return root 
    
    # here if only neither p or q found on the neither left or right =>  so to return that element only we perform below 
    # left is not None => means left consists some element 
    if left:return left
    if right:return right 
    # if left is not None:  # that means here we found one element neither p or q so we return that element 
    #     return left 
    # else:                       # otherwise return the right 
    #     return right
    return None 
  
    
        
root = Treenode(3)
root.left = Treenode(5)
root.right = Treenode(1)

root.left.left = Treenode(6)
root.left.right = Treenode(2)
root.left.right.left = Treenode(7)
root.left.right.right = Treenode(4)

root.right.left = Treenode(0)
root.right.right = Treenode(8)



# ---------------- Select Target Nodes ----------------

p = root.left.right.left      # Node 7      # assigning the target values p and  q like this in a tree

q = root.left.right.right     # Node 4

print(lowest_common_ancestor(root,p,q).val)     #2