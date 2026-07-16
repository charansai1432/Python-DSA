#  a complete binary tree means exact the full binary tree
#  complete Tree == full binary tree        (check once in the internet)
# brute force solution 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.right = Treenode(4)
root.right.left = Treenode(5)
root.right.right = Treenode(6)

#  in brute force approach 

#  here to count the no. of nodes in the BT 
# first tell me to count the no.of nodes to cur_node ==> the cur_node has to know the how nodes are there in the left and right sub tree's
#  to calculate the no. of nodes right 

#  then left,right,root ==> post order 

#  that means at every node we have to calculate the no.of nodes on left and right sub tree's ==> so return 1 + count(left) + count(right) ==> TC=O(n)


# ===================================================== OPTIMAL SOLUTION APPROACH =====================================================
#  there is a solution even better than the TC=> O((logn))*2  => this is the optimal solution 

#  to done with the optimal solution there is a approach ==> 1. calculate the left and right height 
                                                            # 2. if left and right are equal 
                                                            # 3. then we calculate the count = 2^height - 1
                                                            
#  in simple for the optimal solution to calculate the count_no_nodes = 2^height -1 

#  ===========================================================                  ===========================================================

# brute force approach 
def count_of_nodes(root):
    
    if root is None:
        return 0
    
    count_left = count_of_nodes(root.left)
    count_right = count_of_nodes(root.right)
    return 1 + count_left + count_right
   
print(count_of_nodes(root))



# optimal solution approach 

def count_no_of_nodes(root):
    # count = 0
    if root is None:
        return 0 
    left_height = 0
    right_height = 0
    left_node = root
    while left_node:
        left_height += 1
        left_node = left_node.left

    right_node = root
    right_height = 0 
    while right_node:
        right_height += 1
        right_node =  right_node.right


    if left_height == right_height:
        count = 2**left_height - 1
        return count
    
    #when left and right heights doesnot match then the below return statement will execute okk 
    #  here we shouldn't do directly 1 + left_height+ right_height
    #  because here assume if left_height = 2 and right_height = 1 and return will return 1 + 2 + 3 = 5 
    #  but we have only 2 nodes ==> [1,2] ==> root is 1 and left child height is 2 
    
    #  simple read this 2 lines for better understanding
    # Your code starts at the root (1), adds 1 to the height, and moves to the left child (2). 
    # It adds another 1 to the height, tries to move left again, sees None, and stops. Total left path = 2.
    
    #  that's why we did this below return statement
    
    return 1 + count_no_of_nodes(root.left) + count_no_of_nodes(root.right)
      
print(count_no_of_nodes(root))
    


