
# Problem

# Given a binary tree and a target sum,

# Count the number of paths whose sum equals the target.

# Rules:

# ✅ Path can start from any node
# ✅ Path can end at any node
# ✅ Path must always move downward
# ❌ Cannot move upward


# ========================================================================================================================
# Path Sum III
# ANY NODE

# ↓

# ANY NODE

# (Downward only)

# ========================================================================================================================


#  every node can be a starting point of it 

# Pattern Recognition

# This question actually combines two DFS traversals.

# Pattern 1

# Search every node

# Pattern 2

# From that node,
# find all valid downward paths.

# So mentally,

# For Every Node

# ↓

# Start a DFS

# ↓

# Count Paths


# ⭐ Brute Force Idea

# Think like this:

# At every node ask

# Can a valid path start here?

# If yes,

# explore every downward path.

# Then

# move to left subtree,

# move to right subtree,

# and repeat the same process.


## brute force approach 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def count_path(root,target):
    if root is None:
        return  0
    count = 0
    if root.val == target:
        count += 1
    count += count_path(root.left,target - root.val)
    count += count_path(root.right,target - root.val)
    
    return count 

def path_sum(root,target):
    if root is None:
        return 0
    
    count = count_path(root,target)
    
    left = path_sum(root.left,target)
    right = path_sum(root.right,target)
    return count + left + right



root= Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

root.right.left = Treenode(6)
root.right.right = Treenode(7)

print(path_sum(root,7))
        


### optimal solution using the prefix_sum + hashmap technique 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def count_path(root,cur_sum,target,freq):
    
    if root is None:
        return 0
    
    count = 0
    cur_sum += root.val
    
    past_sum = cur_sum - target
    
    if past_sum in freq:
        count += freq[past_sum]
        
    freq[cur_sum] = freq.get(cur_sum,0)+1
    
    count += count_path(root.left,cur_sum,target,freq)
    count += count_path(root.right,cur_sum,target,freq)
    
    
    # back tracking logic 
    freq[cur_sum] -= 1
    
    return count
 
def path_sum_III(root,target):
    
    freq = {0:1}
    return count_path(root,0,target,freq)

root= Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

root.right.left = Treenode(6)
root.right.right = Treenode(7)
        
print(path_sum_III(root,7))


# ⭐ Pattern Recognition (Very Important)

# Whenever you see a Tree problem that asks for:

# Count paths
# Sum equals target
# Paths can start at any node
# Paths must go downward

# Your brain should think:

# Current Sum

# ↓

# Prefix Sum

# ↓

# HashMap

# ↓

# Backtracking

# Not "two DFS" anymore.

# This optimization is one of the strongest examples of transferring an Array technique (Prefix Sum) into a Tree traversal.



# WHY IS PREFIX = {0:1} ?

# Imagine

#       7

# Target = 7

# Current Sum

# 7

# Need

# 7-7

# =

# 0

# If

# 0

# already exists

# We immediately know

# Root itself

# ↓

# forms one valid path.

# That's why we initialize

# {0:1}


# 🌳 The Magic of Backtracking

# Imagine we don't remove prefix sums.

# Suppose we're exploring the left branch:

# 1 → 2 → 4

# The map contains:

# {
# 0:1,
# 1:1,
# 3:1,
# 7:1
# }

# Now we return and go to the right child 3.

# If we leave 7 in the map, the algorithm may think that a prefix from the left branch can be combined with a path in the right branch.

# That's impossible because a valid path must be continuous and downward.

# So before leaving a node, we remove its prefix sum. This keeps the map representing only the current root-to-current-node path.






class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def path_sum_III(root,cur_prefixsum,target,freq):    
    
    if root is None:
        return 0
    
    if freq is None:
        freq = {0:1}
    count = 0 
    cur_prefixsum += root.val
    past_prefix_sum = cur_prefixsum - target
    
    if past_prefix_sum in freq:
        count += freq[past_prefix_sum]
        
    freq[cur_prefixsum] = freq.get(cur_prefixsum,0)+1
    
    left = path_sum_III(root.left,cur_prefixsum,target,freq)
    right = path_sum_III(root.right,cur_prefixsum,target,freq)
    freq[cur_prefixsum] -= 1
    return count + left + right
        
root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(-3)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)

root.left.right.right = TreeNode(1)

root.right.right = TreeNode(11)
print(path_sum_III(root,cur_prefixsum=0,target=8,freq=None))





