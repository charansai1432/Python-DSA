class vertical_order_travarsal:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = vertical_order_travarsal(1)
root.left = vertical_order_travarsal(2)
root.right = vertical_order_travarsal(3)
root.left.left = vertical_order_travarsal(4)
root.left.right = vertical_order_travarsal(5)
root.right.left = vertical_order_travarsal(6)
root.right.right = vertical_order_travarsal(7)


def vertical_order(root):
    columns = {}
    from collections import deque
    queue = deque()
    queue.append((root,0))
    result = []
    while queue:
        
        root,col = queue.popleft()
        if col not in columns:
            columns[col] = []
        columns[col].append(root.val)
        
        if root.left:
            queue.append((root.left,col - 1))
        if root.right:
            queue.append((root.right,col + 1))
        
    for col in sorted(columns):
        result.append(columns[col])
    return result
print(vertical_order(root))
