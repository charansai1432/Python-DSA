class top_view_BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = top_view_BT(1)
root.left = top_view_BT(2)
root.right = top_view_BT(3)
root.left.left = top_view_BT(4)
root.left.right = top_view_BT(5)
root.right.left = top_view_BT(6)
root.right.right = top_view_BT(7)


def top_view(root):                     # return the 1st element in each colums 
    if not root:
        return []
    from collections import deque
    queue = deque()
    queue.append((root,0))
    columns = {}
    result = []
    while queue:
        root,col = queue.popleft()
        if col not in columns:
            columns[col] = root.val
        if root.left:
            queue.append((root.left,col - 1))
        if root.right:
            queue.append((root.right,col + 1))
    for col in sorted(columns):
        result.append(columns[col])
    return result
print(top_view(root))