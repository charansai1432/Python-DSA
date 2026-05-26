

# brute force apporach 
# the time complexity is O(m*n) 
# m is the no. of rows in matrix and n is the no. of cols in matrix 

def search_in_2D_matrix(matrix,target):
    for row in matrix:
        for num in row: 
            if num == target:
                return True
    return False

# print(search_in_2D_matrix([
#  [1,3,5,7],
#  [10,11,16,20],
#  [23,30,34,60]
# ],11))
# print(search_in_2D_matrix([
#  [1,3,5,7],
#  [10,11,16,20],
#  [23,30,34,60]
# ],0))
# print(search_in_2D_matrix([
#  [],
#  [],
#  []
# ],0))


# optimal solution approach using the binary search
# the optimal solution can be done using the binary search technique 
# => the time complexity now is O(log (m * n))

def search_in_2D_matirx(matrix,target):
    
    rows = len(matrix)
    cols = len(matrix[0])
    l = 0 
    r = rows*cols - 1
    while l <= r:
        mid = l + (r-l)//2
        row = mid // cols
        col = mid % cols 
        
        value = matrix[row][col]
        if value == target:
            return True
        elif value < target:
            l = mid + 1
        else:
            r = mid - 1
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
