
class right_side_view_BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = right_side_view_BT(1)
root.left = right_side_view_BT(2)
root.right = right_side_view_BT(3)
root.left.left = right_side_view_BT(4)
root.left.right = right_side_view_BT(5)
root.right.left = right_side_view_BT(6)
root.right.right = right_side_view_BT(7)

def right_view(root):       # last_most_element at each level 
    if  not root:
        return []
    result = []
    from collections import deque
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            root = queue.popleft()
            if i == level_size - 1:
                result.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
    return result
print(right_view(root))