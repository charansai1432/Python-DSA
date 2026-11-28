#
#               Pattern Recognition 
# 
# How do we recognise this interview pattern?
# Look for these keywords:
# - Detect a cycle in a directed graph.
# - Check whether a directed graph is cyclic.
# - Determine whether there is a circular dependency.
# - Find whether a sequence of directed connections returns to an earlier node.


# DFS approach 
#  recrsuively traval in the node neighbour to determive cycle 
#  here we use the two arrays which are visited and recrusive path 
#  the visited array which keeps tracks of visited nodes in the grahp 
#  the recrusive path which helps to determine the cur_node is aleady present in the recrusive path if present then cycle exists other wise no cycle exists 
def detect_cycle_in_directed_graph(adj):
    n = len(adj)
    
    visited = [False]*n 
    recrusive_path = [False]*n
    
    def dfs(node):
        visited[node] = True 
        recrusive_path[node] = True 
        for neighbour in adj[node]:
            if not visited[neighbour]:
                if dfs(neighbour):
                    return True 
            elif recrusive_path[neighbour]:
                return True 
        recrusive_path[node] = False
        return False 
    for node in range(n):
        if not visited[node]:
            if dfs(node):
                return True
    return False    
    
    
print(detect_cycle_in_directed_graph(adj=[[1, 2], [2], [3], []]))



# BFS approach using kahn's algorithm 

#  kahn's algo is used in mainly detection of cycle in directed_graph 
#  kahn's algo mainly used in the topological sorting okk 
#  

#  approach --> 
# 
# 1st we have to calculate the indegree of all vertex's in a graph 
#  after that we have find the indegree of nodes whose are having the '0' value 
#  inside the queue we store the node having the '0' value 
# after that normal BFS approach 
#  pop the node in the queue --> then increment the proccessed variable by '1' 
#  if the node having an neighbours --> we decrement the indegree value by 1 
#  after decrementing value by '1' --> if the node indegree became '0' --> store in the queue 

#  Finally --> if the processed nodes != no. of vetex --> return True i.e cycle exists
# other wise return False.

#  here the question is directed graph i.e every node definately should be connected with the other node atleast '1' time ..
#  that there is a cycle right 

#  so we are poping out the nodes with the indegree value '0' --> because that means there is no incoming edge coming to that node.




def detect_cycle_in_directed_grap(adj):
    n = len(adj)
    indegree = [0]*n
    
    from collections import deque 
    queue = deque()
    
    for node in range(n):
        for neighbour in adj[node]:
            indegree[neighbour] += 1
            
    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)
        
    # normal bfs approach 
    
    processed = 0
    while queue:
        node = queue.popleft()
        processed += 1
        for neighbour in adj[node]:
            indegree[neighbour] -= 1 
            
            if indegree[neighbour] == 0:
                queue.append(neighbour)
                
    if processed < n:return True 
    else:
        return False 
print(detect_cycle_in_directed_grap(adj=[[1, 2], [2], [3], []]))