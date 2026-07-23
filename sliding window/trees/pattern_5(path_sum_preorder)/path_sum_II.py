
# here it's a question like where we keep track of 2 things 
    # 1. cur_sum
    # 2. cur_path 
    
# in the previous path_sum question we will calculate the cur_sum till the cur_node only.
#  in the binary_path_sum question we keep track of cur_sum and it's path when cur_sum match's the target we will return the that exact path for it.

# optimal solution 

#  in this question we keep track 
    # 1. cur_sum and cur_path 
#  if the cur_sum mathcs the target we store the cur_path for that one 

# that's it the question is 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)

root.left.left = Treenode(10)
root.left.right = Treenode(5)

root.right.left = Treenode(6)
root.right.right = Treenode(7)

def path_sum_II(root,cur_sum,target,path = None,result = None):
    
    
    # create the path and result once again 
    # {VVVIMP} if we create something like path and result = []
    #  it's wrong like for every recursive call the path and result gets a new list 
    #  so final return statement we get the empty list 
    
    if path is None:            # initally we dont the have the path so creating a empty list for only once 
        path = []
        
    if result is None:      # same as path comments okkk
        result = []
    
    if root is None:        # base condition ==> is root is None i.e empty tree such case the result also be empty only 
        return result
    
    cur_sum += root.val         # cur_node process 1st ==> i.e pre-order traversal technique for this question path_sum_II (cur_sum + cur_path)
    path.append(root.val)       
    
    if root.left is None and root.right is None:        # leaf node condition ==> check with the cur_sum with target 
        if cur_sum == target:
            result.append(path.copy())                          # if match's store the answer in a result list as a copy of the path for every matching target {VVIMMP} as a copy of path okk ==> NOT directly storing the path okk ==> we are making a copy of it 
    
    path_sum_II(root.left,cur_sum,target,path,result)           # recrusion func for left and right one --> to traval in entire carry and along with carry the target ,path,cur_sum
    path_sum_II(root.right,cur_sum,target,path,result)
    
    path.pop()          # backtracking logic ==> to check the another path of the cur_node of left/right we use the backtrack here 
                            # Remove the current node before returning to the parent
                            # so the path is restored for exploring another branch.
                            
    return result           # finally return the answer 
print(path_sum_II(root,cur_sum=0,target=7))


# =========================================================={VVIMP}===========================================================

# path and result are mutable objects.
# Using [] as default arguments causes Python to reuse
# the same list across different function calls.
# So we use None and create the list only once.