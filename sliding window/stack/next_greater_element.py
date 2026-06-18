

# Here the actual questions is here we have to find 1st greater element of every element on the "RIGHT SIDE"
# if the element right side is at last element then keep the it as "-1"


# brute force apporach 

def next_greater_element(arr):
    n = len(arr)
    
    result = [-1]*n                     # create a result with all elements as [-1,-1,-1]
    
    for i in range(n):
        
        for j  in range(i+1,n):             # comparing the next element to cur_element (i+1)
            if arr[j] > arr[i]:             # compare the values 
                result[i] = arr[j]              # if greater value place in the result list 
                break                       # break ==> we want the 1st greater element
             
    return result
print(next_greater_element([1,2,3]))

# optimal solution approach 

# how it is stack pattern ==> if in a question  says the next greater,smaller,previous greater,smaller element 
# think like stack pattern 

# VVVVIMP{Here in the stack => we store "{INDEX}" ==> why ? => next greater element question we used to store with index only STANDARD LOGIC }

# {if any cur_ele is greater than top element in stack ==> then we pop it and in that index we add the cur_ele to the result list }

def next_greater_element(arr):
    n = len(arr)
    stack =  []                                 #
    result = [-1]*n                 # if like this if we have used "REMEMBER WITH THE INDEX POSITION ONLY WE CAN CHANGE THE RESULT LIST "
    
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:        # condition tell the cur_ele > element present inthe stack 
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)                 # at intially stack is empty => at starting we don't have any thing in stack so append it.
    return result

print(next_greater_element([1,2,3]))

