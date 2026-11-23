
# Imagine there are n cities. Some cities are directly connected to each other, and some are indirectly connected through other cities.

# We need to find the total number of provinces.

# A province is a group of cities where every city is connected to every other city in that group, either directly or indirectly

# Here:
# - City 0 is connected to city 1.
# - City 2 is not connected to either city.

# Therefore, there are 2 provinces.


# Pattern recognition – How do we identify this problem?

# Look at these clues:
# - We are given multiple cities.
# - Some cities are connected.
# - Connections can be direct or indirect.
# - We need to count the number of separate groups.
# Whenever an interview question asks you to count separate groups of connected nodes, think:

# {VVVIMP} {Connected Components} --> connected components can be directed or indirected 
# DFS / BFS
# One traversal for each group of nodes that has not already been visited.


def no_of_provinces(adjacency_matix):
    
    pass
    
adjacency_matrix =  [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(no_of_provinces(adjacency_matrix))