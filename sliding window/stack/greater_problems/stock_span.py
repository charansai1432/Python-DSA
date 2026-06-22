
# same as previous greater element question in the brute force approach only if condition changes

# brute force approach 

def stock_span(arr):
    
    n  = len(arr)
    result = [0]*n
    for i in range(n):
        span = 1
        for j in range(i-1,-1,-1):
            if arr[j] <= arr[i]:
                span += 1       # here in the previous greater element question we immediately return the "BREAK" statememt after the condition 
                            # but here we want "ALL THE VALID RANGE ELEMENTS" from the backward
                            # not just the 1st greater element ==> we want all valid days range so keep the else condition with "BREAK" keyword separately
            
            else:           # in  the above i have written the logic                     
                break
            
        result[i] = span 
    return result

print(stock_span([100, 80, 60, 70, 60, 75, 85]))
    
# optimal solution approach 


def stock_span(arr):
    n =  len(arr)
    result = [0]*n
    stack = []
    span = 1
    for i in range(n):

        while stack and arr[stack[-1]] <= arr[i]:
           stack.pop()
           
        if stack:
            result[i] = i - stack[-1]
            
        else:       # that means if stack doesn't contains any elements that means the valid range is given by  i + 1 in simple terms the length from the index to current is i + 1 if i = 0 i.e the cur_stack is maximum traded here 
            result[i] = i + 1
            
        stack.append(i)
        
    return result
            
            
print(stock_span([100, 80, 60, 70, 60, 75, 85]))

print(stock_span([30,40,35,50]))


# indexing.If the stack is completely empty after the while loop finishes, it means every single element before day i was smaller than or equal to today's price. Therefore, the span includes today plus all the previous days.Let’s look at the math using the index i:At Day Index i = 0 (The 1st day): 
# The stack is empty.$$\text{Span} = 0 + 1 = 1 \text{ day (just itself)}$$At Day Index i = 3 (The 4th day): 
# If the price on day 3 is higher than everything before it, it means day 0, day 1, day 2, and day 3 are all part of the span.$$\text{Span} = 3 + 1 = 4 \text{ days}$$i + 1 is simply the mathematical formula 
# to find the total number of elements from the beginning of the array up to the current index.