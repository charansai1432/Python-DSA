class cousins_in_BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = cousins_in_BT(1)
root.left = cousins_in_BT(2)
root.right = cousins_in_BT(3)
root.left.left = cousins_in_BT(4)
root.left.right = cousins_in_BT(5)
root.right.left = cousins_in_BT(6)
root.right.right = cousins_in_BT(7)


def cousins_BT(root,x,y):
    if not root:
        return False
    from collections import deque
    queue = deque()
    queue.append((root,None))
    while queue:
        x_parent = None
        y_parent = None
        level_size = len(queue)
        for i in range(level_size):
            root,parent = queue.popleft()
            if root.val == x:
                x_parent = parent
            if root.val == y:
                y_parent = parent 
                
            if root.left:
                queue.append((root.left,root))
            if root.right:
                queue.append((root.right,root))
        
        if x_parent is not None or y_parent is not None:            # atleast one x either y is found but not at same level even though atleast we found one element 
            if x_parent is not None and y_parent is not None:           # both x and y is found at same level and checking whether their parent values are same or different
                return x_parent != y_parent             # if different return True 
            return False                            # 
print(cousins_BT(root,4,6))



# Only one of the nodes is found at a level

# Example: if you’re searching for x=4 and y=8, and only 4 exists in the tree but 8 doesn’t.

# At the level where 4 is found, x_parent is set but y_parent stays None.

# Since one is found but not both, the function returns False.

# Both nodes are found but not at the same level

# The check if x_parent is not None or y_parent is not None: ensures that as soon as one of them is found at a level, you evaluate.

# If both aren’t found together at that level, the function returns False.

# Example: searching for x=4 and y=6 in your tree. 4 is found at level 2 under parent 2, but 6 is found at level 3 under parent 3. Since they’re not at the same level, the function returns False.