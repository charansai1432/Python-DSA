
# bi_partite is a graph   --- > coloring pattern 

#           -> where two connected nodes shouldn't have the same group or color 

        #  i.e the two connected nodes shouldn't lies in the same group or color 
  
#   the two adjacnet nodes should not have same color or group if same color or group is there then it isn't a bi_partite graph 
# 
# 
#  -1 -> till not visited
#  0 ->  red/blue color or group 0/group1 


# BFS approach 
def graph_bipartite(adj):
    n = len(adj) 
    
    color = [-1]*n              # visited set as normal in the BFS/DFS approach's 
    from collections import deque
    queue = deque()
    
    for start in range(n):
        
        if color[start] != -1:  # the node is already visited 
            continue
        
        color[start] = 0    # making the 1st node in the adjacency list into the red/blue color or group0/group1 
        
        queue.append(start) 
        
        # normal BFS 
        
        while queue:
            node = queue.popleft()          # now we have check for the neighbour's 
            for neighbour in adj[node]:
                
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    queue.append(neighbour)
                    
                elif color[neighbour] == color[node]:
                    return False 
                
        return True 
# print(graph_bipartite(adj=[[1,2,3],[0,2],[0,1,3],[0,2]]))
print(graph_bipartite(adj=[[1,3],[0,2],[1,3],[0,2]]))

# DFS approach 
def graph_bi_partite(adj):
    n = len(adj)
    
    color =[-1]*n
    
    
    def dfs(node):
        # color[node] = 0 
        
        for neighbour in adj[node]:
            
            if color[neighbour] == -1:
                color[neighbour] = 1  - color[node]
                dfs(neighbour)
            elif color[neighbour] == color[node]:
                return False 
        return True 
    
    
    for node in range(n):
        
        if color[node] == -1:
            
            color[node] = 0 
            
        if  not dfs(node):
           return False  
    return True  
            
        
print(graph_bi_partite(adj=[[1,3],[0,2],[1,3],[0,2]]))    
    