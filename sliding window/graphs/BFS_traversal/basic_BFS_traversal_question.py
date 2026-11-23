
def BFS_traversal_question(graphs,start):
    
    from collections import deque
    queue = deque([start])
    
    visited = set()
    visited.add(start)
    result = []
    while queue:
        node = queue.popleft()
        
        result.append(node)
        for neighbour in graphs[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return result 
graphs ={
    1:[2,3],
    2:[1,4,5],
    3:[1,6,7],
    4:[2],
    5:[2],
    6:[3],
    7:[3]
}
start = 1
print(BFS_traversal_question(graphs,start))

