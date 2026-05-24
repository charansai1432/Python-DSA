

# brute force apporach 

def search_in_2D_matrix(matrix,target):
    for row in matrix:
        for num in row: 
            if num == target:
                return True
    return False
print(search_in_2D_matrix([
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
],11))
print(search_in_2D_matrix([
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
],0))
print(search_in_2D_matrix([
 [],
 [],
 []
],0))


# optimal solution approach using the binary search

def search_in_2D_matirx(arr,target):
    
    
    pass
    
print(search_in_2D_matrix([
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
],11))
