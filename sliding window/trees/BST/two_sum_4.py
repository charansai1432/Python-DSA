
class two_sum_4:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
root = two_sum_4(5)
root.left = two_sum_4(3)
root.right = two_sum_4(6)

root.left.left = two_sum_4(2)
root.left.right = two_sum_4(4)

root.right.right = two_sum_4(7)

def two_sum_four(root,k):
    result = []
    def inorder(root):
        if root is None:return 
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)
    inorder(root)
    
    l = 0
    r = len(result) - 1
    
    while l < r:
        cur_sum = result[l] + result[r]
        
        if cur_sum == k:
            return True 
        elif cur_sum < k:
            l += 1
        
        else:
            r -= 1
    return False
print(two_sum_four(root,9))
            