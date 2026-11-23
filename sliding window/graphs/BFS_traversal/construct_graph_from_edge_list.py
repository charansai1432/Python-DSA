
#  here we solved this question from the edge list to adjacency list 
# image edge list tell us like --> from the veterx 0 / node 1 connected to this node like that
#  adjacency list -- > for this vertex this are our neighbours 

def construct_a_graph_from_edge_list_to_undirected_graph(edges):
    
    freq = {}
    
    for u , v in edges:
        if u not in freq:
            freq[u] = []
        if v not in freq:
            freq[v] = []
            
        freq[u].append(v)
        freq[v].append(u)
    return freq

edges = [
    [0,1],
    [0,2],
    [1,3],
    [2,4]
]
print(construct_a_graph_from_edge_list_to_undirected_graph(edges))

print("\n")

def construct_a_graph_from_edge_list_to_directed_graph(edges):
    
    freq = {}
    
    for u , v in edges:
        if u not in freq:
            freq[u] = []
        if v not in freq:
            freq[v] = []
            
        freq[u].append(v)
        
    return freq

edges = [
    [0,1],
    [0,2],
    [1,3],
    [2,4]
]
print(construct_a_graph_from_edge_list_to_directed_graph(edges))
    
    
print("\n")
    
def construct_a_graph_from_edge_list_to_undirected_weightend_graph(edges):
    
    freq = {}       # adjacency list 
    
    for u , v , weight in edges:
        
        if u not in freq:
            freq[u] = []
        if v not in freq:
            freq[v] = []
        
        freq[u].append((v,weight))
        freq[v].append((u,weight))
    return freq 
edges = [
    [0,1,5],
    [0,2,3],
    [1,3,7]
]
print(construct_a_graph_from_edge_list_to_undirected_weightend_graph(edges))
    
print("\n")

   
def construct_a_graph_from_edge_list_to_directed_weightend_graph(edges):
    
    freq = {}       # adjacency list 
    
    for u , v , weight in edges:
        
        if u not in freq:
            freq[u] = []
        if v not in freq:
            freq[v] = []
        
        freq[u].append((v,weight))
        
    return freq 
edges = [
    [0,1,5],
    [0,2,3],
    [1,3,7]
]
print(construct_a_graph_from_edge_list_to_directed_weightend_graph(edges))


    
    
    
    
    