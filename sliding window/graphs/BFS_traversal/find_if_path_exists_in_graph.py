

#  here it is undirected graph 
def find_if_path_exists_in_graph(edges,source,destination):
    
    #  converting a edge list into a adjacency list 
    freq = {}
    for u , v in edges:
        if u not in freq:
            freq[u] =[]
        if v not in freq:
            freq[v] = []
        freq[u].append(v)
        freq[v].append(u)
        
    # BFS approach 
    
    from collections import deque
    
    queue = deque([source])
    visited = set()
    visited.add(source)
    while queue:
        node = queue.popleft()
        
        if node == destination:
            return True 
        
        for neighbour in freq.get(node,[]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return False
    
edges = [
    [0,1],
    [0,2],
    [3,5]
]
source =0
destination = 5 
print(find_if_path_exists_in_graph(edges,source,destination))



#  we can also implement the question using the DFS approach too --> using recrusion 


def find_if_path_exists_in_grap(edges,source,destination):
    
    #  converting a edge list into a adjacency list 
    freq = {}
    for u , v in edges:
        if u not in freq:
            freq[u] =[]
        if v not in freq:
            freq[v] = []
        freq[u].append(v)
        freq[v].append(u)
        
    # DFS approach 
    visited = set()
    def dfs(node):
        
        if node == destination:
            return True 
        
        visited.add(node)
        for neighbour in freq.get(node,[]):
            if neighbour not in visited:
                if dfs(neighbour):
                    return True 
        return False 

    return dfs(source)

edges = [
    [0,1],
    [0,2],
    [3,5]
]
source =0
destination = 5 
print(find_if_path_exists_in_grap(edges,source,destination))