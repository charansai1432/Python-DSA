

class Treenode:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def good_nodes(root,max_val_seen_so_far = float('-inf')):
    
    count = 0
    
    if root is None:
        return 0
    
    if root.val >= max_val_seen_so_far:
        count += 1
    # max_val_seen_so_far = float('-inf')
    max_val_seen_so_far = max(max_val_seen_so_far,root.val)             # parent -> child ==> top - bottom 
    
    # this question is basically both top-bottom & bottom - top approach's 
    
    left_count = good_nodes(root.left,max_val_seen_so_far)
    right_count = good_nodes(root.right,max_val_seen_so_far)
    
    return count + left_count + right_count         # i.e left , right, cur ==> post order ==> bottom-up 

root = Treenode(3)
root.left = Treenode(1)
root.right = Treenode(4)
root.left.left = Treenode(3)
root.right.right = Treenode(5)

print(good_nodes(root))             #4

    
    
    