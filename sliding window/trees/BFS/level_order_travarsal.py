
class level_order_travarsal:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = level_order_travarsal(1)
root.left = level_order_travarsal(2)
root.right = level_order_travarsal(3)
root.left.left = level_order_travarsal(4)
root.left.right = level_order_travarsal(5)
root.right.left = level_order_travarsal(6)
root.right.right = level_order_travarsal(7)



# Here we will travarse the each element by row by row 

def level_order_travarse(root):
    from collections import deque
    
    if not root:            # if tree is empty ==> return the empty (according to question return okk)
        return None
    queue = deque()
    
    queue.append(root)
    
    while queue:
        root = queue.popleft()
        print(root.val,end=" ")
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
level_order_travarse(root)

