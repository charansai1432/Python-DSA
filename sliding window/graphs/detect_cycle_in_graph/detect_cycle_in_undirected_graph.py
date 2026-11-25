#  v is no. of vertex's
# adj  is edge list 

def detect_cycle_in_undirected_graph(adj):

    visited = [False]*n
    
    def dfs(node,parent):
        visited[node] = True 
        for neighbour in adj[node]:
            if not visited[neighbour]:
                if dfs(neighbour,node):
                    return True 
            elif neighbour != parent:
                return True 
        return False 
            
    
    
    
    for node in range(n):
        if not visited[node]:
            if dfs(node,-1):
                return True 
    return False 
            
    
    
adj = [
    [1,2],
    [0,2],
    [0,1]
]
n = len(adj)   

print(detect_cycle_in_undirected_graph(adj))