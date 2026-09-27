

class level_by_level_travarsal:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = level_by_level_travarsal(1)
root.left = level_by_level_travarsal(2)
root.right = level_by_level_travarsal(3)
root.left.left = level_by_level_travarsal(4)
root.left.right = level_by_level_travarsal(5)
root.right.left = level_by_level_travarsal(6)
root.right.right = level_by_level_travarsal(7)


def level_by_level_travarse(root):
    answer = []
    from collections import deque
    
    queue = deque()
    
    queue.append(root)
    
    while queue:
        cur_list = []
        level_size = len(queue)
        for i in range(level_size):
            root = queue.popleft()
            cur_list.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        answer.append(cur_list)
    return answer
print(level_by_level_travarse(root))
        