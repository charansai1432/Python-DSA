class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        
root = Node(5)
root.left = Node(10)
root.right = Node(8)
root.left.left = Node(20)
root.left.right = Node(15)

def insertion_in_minheap(root):
    