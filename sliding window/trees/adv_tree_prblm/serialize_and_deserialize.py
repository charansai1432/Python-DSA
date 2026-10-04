class serialize_and_de_serialize:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
        
root = serialize_and_de_serialize(1)
root.left = serialize_and_de_serialize(2)
root.right = serialize_and_de_serialize(3)
root.right.left = serialize_and_de_serialize(4)
root.right.right = serialize_and_de_serialize(5)

def searlize(root):
    result = []
    def dfs(root):
        if root is None:
            result.append("#")
            return 
        result.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ",".join(result)
print(searlize(root))



def desearlize(data):
    values  = data.split(",")
    
    index = 0
    def dfs():
        nonlocal index
        if values[index] == "#":
            
            index += 1
            return None
        
        root_value = int(values[index])
        
        root = serialize_and_de_serialize(root_value)
        index += 1
        root.left = dfs()
        root.right = dfs()

        return root
    return dfs()
data = searlize(root)
print(desearlize(data))

root = desearlize(data)

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
inorder(root)


