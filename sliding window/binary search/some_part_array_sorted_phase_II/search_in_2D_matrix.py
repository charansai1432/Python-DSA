# here in the 2D-matrix we have to find the target in a matrix 


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
# [ [1,3,5,7], [10,11,16,20], [23,30,34,60] ]
# [ [row1], [row2], [row3]] = len(matirx) = 3
#  colums present inside a row      [ [c1,c2,c3] , [c1,c2,c3] , [c1,c2,c3] ] here that means the length of colums can be given by cols = len(matrix[0])

# cols = len(matrix[0]) ===> here matrix[0] gives the [c1,c2,c3] and now the length of this c1,c2,c3 is 3 


def search_in_2D_matirx(matrix,target):
    
    rows = len(matrix)                      # here the length of rows is given by the len(maritx)
    cols = len(matrix[0])                           # refer the above one for the rows and colums technique 
    
    l = 0               # l = 0 that means from the index position 
    r = rows*cols - 1       # in a 2D matrix the last element is r = rows*cols - 1 
    
    while l <= r:
        
        mid = l + (r-l)//2
        
        row = mid // cols           # this two formula's helps to pinpoint the target element in a matrix 
        col = mid % cols 
        
        value = matrix[row][col]        # i.e the above row and col gives the cooridates in a matrix for a target 
        
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
