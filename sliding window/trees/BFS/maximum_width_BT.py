class maximum_width:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = maximum_width(1)
root.left = maximum_width(2)
root.right = maximum_width(3)
root.left.left = maximum_width(4)
root.right.right = maximum_width(7)

def maximum_width_BT(root):
    if not root:
        return 0
    
    max_width =  float('-inf')
    from collections import deque
    queue = deque()
    queue.append((root,1))
    
    while queue:
        # root,index = queue.popleft()
        
        first_pos = 0
        last_pos = 0
        level_size = len(queue)
        for i in range(level_size):
            root,index = queue.popleft()
            
            if i == 0:
                first_pos = index
            if i == level_size - 1:
                last_pos = index
                
            if root.left:
                queue.append((root.left,2*index ))
            if root.right:
                queue.append((root.right,2*index + 1))
                
        width = last_pos - first_pos + 1
        max_width = max(max_width,width)
    return max_width
print(maximum_width_BT(root))