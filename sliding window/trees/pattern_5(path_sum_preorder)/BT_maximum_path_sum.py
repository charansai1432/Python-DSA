

# # optimal solution approach 

# class Treenode:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None
# # global max_sum
# def dfs(root,max_sum):
#     # nonlocal max_sum
#     if root is None:
#         return 0 
    
#     left_gain = max(0,dfs(root.left,max_sum))
#     right_gain = max(0,dfs(root.right,max_sum))
    
#     cur_path = root.val + left_gain + right_gain
#     max_sum = max(max_sum,cur_path)
    
#     return root.val + max(left_gain,right_gain)
    
# def maximum_path_sum(root):
#     max_sum = float('-inf')
#     def dfs(root):
#     # nonlocal max_sum
#         if root is None:
#             return 0 
    
#         left_gain = max(0,dfs(root.left))
#         right_gain = max(0,dfs(root.right))
    
#         cur_path = root.val + left_gain + right_gain
#         max_sum = max(max_sum,cur_path)
    
#         return root.val + max(left_gain,right_gain)
#     dfs(root)
#     return max_sum

        
# root = Treenode(1)
# root.left = Treenode(2)
# root.right = Treenode(3)

# root.left.left = Treenode(4)
# root.left.right = Treenode(5)

# root.right.left = Treenode(6)
# root.right.right = Treenode(7)
# print(maximum_path_sum(root))



# optimal solution again practise finally 
# Binary Tree Maximum Path Sum
#
# Pattern:
# 1. Postorder DFS
# 2. Global Variable
# 3. Ignore Negative Paths
#
# In this question:
# - Path can start from ANY node.
# - Path can end at ANY node.
# - Path cannot split while returning to parent.
# - At every node we calculate:
#     1. What should I return to my parent?
#     2. Is this node the center of the maximum path?
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        


max_sum = float('-inf')
def max_path_sum(root):
    
    global max_sum
    if root is None:
        return 0 
    
    left_side = max_path_sum(root.left)
    right_side = max_path_sum(root.right)
    
    left = max(0,left_side)
    right = max(0,right_side)
    
    cur_path = root.val + left + right
    max_sum = max(max_sum,cur_path)
    
    return root.val + max(left,right)
        
root = TreeNode(-10)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
max_path_sum(root)
print(max_sum)