#  v is no. of vertex's
# adj  is edge list 

# BFS approach 
from collections import deque

def is_cycle(V, adj):

    visited = [False] * V

    for start in range(V):

        if not visited[start]:

            queue = deque([(start, -1)])
            visited[start] = True

            while queue:

                node, parent = queue.popleft()

                for neighbour in adj[node]:

                    if not visited[neighbour]:

                        visited[neighbour] = True

                        queue.append((neighbour, node))

                    elif neighbour != parent:

                        return True

    return False


adj = [
    [1, 2],
    [0, 2],
    [0, 1]
]

print(is_cycle(3, adj))


# DFS appraoch 
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



# practising again to remember the logic 

# BFS approach 

def detect_cycle_in_ungraph(adj):
    from collections import deque
    queue = deque()
    
    n = len(adj)
    
    visited = [False] * n 
    
    for node in range(n):
        
        if not visited[node]:
            visited[node] = True 
            queue.append((node,-1))
            
            while queue:
                node,parent  = queue.popleft()
                
                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True 
                        
                        queue.append((neighbour,parent)) 
                        
                    elif neighbour != parent :
                        return True 
    return False 
print(detect_cycle_in_ungraph(adj=[
    [1, 2],
    [0, 2],
    [0, 1]
]))

# DFS approach 

def detect_cycle_in_ugraph(adj):
    n = len(adj)
    visited = [False]*n
    
    def dfs(node,parent):
        visited[node] = True 
        
        for neighbour in adj[node]:
            if not visited[neighbour]:
                
                if dfs(neighbour,node):         # this just makes the node to visited -> node to True 
                    return True 
                
                elif neighbour != parent:           # this condition helps us to detect the cycle in the graph 
                    return True 
        
        return False            # return false -> if no cycle present in the graph 
    
    
    for node in range(n):
        if not visited[node]:
            if dfs(node,-1):
                return True 
    return False 
print(detect_cycle_in_ugraph(adj= [
    [1, 2],
    [0, 2],
    [0, 1]
]))