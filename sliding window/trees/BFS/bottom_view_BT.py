class bottom_view_BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = bottom_view_BT(1)
root.left = bottom_view_BT(2)
root.right = bottom_view_BT(3)
root.left.left = bottom_view_BT(4)
root.left.right = bottom_view_BT(5)
root.right.left = bottom_view_BT(6)
root.right.right = bottom_view_BT(7)


def bottom_view(root):
    if not root:
        return []
    from collections import deque
    queue = deque()
    queue.append((root,0))
    result = []
    columns = {}
    while queue:
        root,col = queue.popleft()
        columns[col] = root.val 
        if root.left:
            queue.append((root.left,col - 1))
        if root.right:
            queue.append((root.right,col + 1))
    for col in sorted(columns):
        result.append(columns[col])
    return result
print(bottom_view(root))