class Next_Right_Pointers_Each_Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None
        
root = Next_Right_Pointers_Each_Node(1)
root.left = Next_Right_Pointers_Each_Node(2)
root.right = Next_Right_Pointers_Each_Node(3)
root.left.left = Next_Right_Pointers_Each_Node(4)
root.left.right = Next_Right_Pointers_Each_Node(5)
root.right.left = Next_Right_Pointers_Each_Node(6)
root.right.right = Next_Right_Pointers_Each_Node(7)


def Right_Pointers_Each_Node(root):
    if not root:
        return None
    
    from collections import deque
    queue = deque()
    queue.append(root)
    while queue:
        previous = None
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            
            if previous is not None:
                previous.next = current
            previous = current
            
            if root.left:
                queue.append(root.left)
            
            if root.right:
                queue.append(root.right)
                
        previous.next = None
        return root 
print(Right_Pointers_Each_Node(root))