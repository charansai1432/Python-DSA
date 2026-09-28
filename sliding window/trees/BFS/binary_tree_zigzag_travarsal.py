
class zig_zag_traversal:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = zig_zag_traversal(1)
root.left = zig_zag_traversal(2)
root.right = zig_zag_traversal(3)
root.left.left = zig_zag_traversal(4)
root.left.right = zig_zag_traversal(5)
root.right.left = zig_zag_traversal(6)
root.right.right = zig_zag_traversal(7)



def zig_zag(root):
    if not root:
        return []
    left_to_right = True
    from collections import deque
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        cur_level = []
        level_size = len(queue)
        for _ in range(level_size):
            root = queue.popleft()
            cur_level.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        if not left_to_right:
            cur_level.reverse()
        result.append(cur_level)
        left_to_right = not left_to_right
    return result
print(zig_zag(root))

