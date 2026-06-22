

# in this question we have to find the 1st previous greater element to the cur_element to the left side 

# if it's the "STARTING ELEMENT" so left element is nothing so return the "-1"

# brute force approach 

def previous_greater_element(arr):
    n = len(arr)
    result = [-1]*n
    for i in range(n):
        for j in range(i-1,-1,-1):          # previous element so we have to move towards back so we used the {-1,-1,-1}
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break                   # immediately break the loop after getting the previous greater element ..why ? ==> we want the 1st previous greater element 
            
    return result
print(previous_greater_element([2,1,0]))


# in the previous greater element ==> in the stack we used to "{store the value}" inside it.

#  for the {previous greater element => store value and compare with cur_element => pop it => and still stack has elements then stack[-1] has the previous grearter element }

# for the {next greater element } => store the index value in stack => if cur_element is greater than the stack => pop with index position => and with that index position we insert into the result list and here cur_ele is {"next greater element"}  to result list 

# optimal solution approach

def previous_greater_element(arr):
    
    n = len(arr)
    stack = []
    result = [-1]*n
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:        # same logic as next greater element but instead of returning the idx and attaching to the result we simple pop it ===> why ?? ===> here in this question 
                                                            # we have to go backward na ==> so if pop one element is lost ==> that means {VVVVIMP} removing the small elements to get the previous greater element 
            stack.pop()         # WE pop the element above condition why ? small element than the cur_ele that the previous element ever be the greater element for the cur_element
        
        if stack:               # even after poping the elements if stack still have elements 
            result[i] = arr[stack[-1]]          # Then simple element at top of the stack is previous greater element to the index of the result list 
        
        stack.append(i)
    return result
    
print(previous_greater_element([2,1,0]))


# If the array contains duplicate elements (e.g., [2, 2, 1]), your code will treat the first 2 as the previous greater element for the second 2.

# Usually, "greater" means strictly greater. To fix this, change < to <= in your loop