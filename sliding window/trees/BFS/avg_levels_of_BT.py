class avg_levels_of_BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = avg_levels_of_BT(10)
root.left = avg_levels_of_BT(5)
root.right = avg_levels_of_BT(15)
root.left.left  = avg_levels_of_BT(2)
root.left.right = avg_levels_of_BT(8)

def avg_levels_of_tree(root):
    if not root:
        return 
    
    from collections import deque
    
    queue = deque()
    queue.append(root)
    answer = []
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        for i in range(level_size):
            root = queue.popleft()
            level_sum += root.val
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        avg = level_sum/level_size
        answer.append(avg)
    
            
    return answer
print(avg_levels_of_tree(root))