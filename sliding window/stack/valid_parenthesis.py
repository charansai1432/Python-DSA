

#  Generally stacks are used to to remember the last element 

# optimal solution 

# when ever a question says brackets or parenthesis or nested brackets immediately think it is stack pattern 

# in the stack questions we do 2 things depending on the requirements 
        # 1. store values in stack 
        # 2. store Index's in stack 
        
# Here in this question how it's stack pattern tell me 
        # 1. here to solve this question the stack is LIFO => last in first out principle 
        # 2. here in this question => the opening paranthesis are stored in the stack 
        # 3. if the closing bracket is comed while iterating => we will pop top element in the stack  => and return true 
        # 4. if the len of stack is 0 ==> return false 
        
# (,[,{ image in a stack i.e 
# | { |
# | [ |
# | ( |

# now we placed the all elements inside a stack ==> which element you close first that would be the "{" ==> because in stack last element get's popped out so we close the last element first 

# i.e last element is opened 
# i.e last element is closed        >>> which resembles to the stack pattern right 

# Here for the optimal solution ==> which bracket was opened most recently ==> we close that first   {vvvimp} stack pattern 

# now in the question main points are 
# 1. here we are just storing the opening brackets in to the stack 
# 2 if the closing bracker is comed ==> we have to check with the top element in stack if same return True 
# 3. after returning true ==> pop it out 
# 4. and last if len(stack) is 0 return true  

# Opening bracket  -> Push
# Closing bracket  -> Match with top
# Match -> Pop
# Mismatch -> False 

# optimal 
def valid_parenthesis(s):
    mappings = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)        # pass only the opening brackets into the stack 
        else:
            
            if not stack:           # if stack doesnot contain any element return false
                return False
            
            if stack[-1] == mappings[ch]:      # that means the top most element and freq_map element which gives the same element i.e '(' == '(' i.e exact same symbol that means a valid pair is found if same we have to pop the top element from the stack 
                
                stack.pop()                 # if mismatch is happend remove the top element from the stack 
            
            elif stack[-1] != mappings[ch]:# if the top element '([{'  doesnot match with current ch or mappings ===> mismatch ==> false
                # ( != ( ==>   not a valid pair in a string
                    return False
    return len(stack) == 0              # if stack having no elements after poping the element from the stack above return true ==> i.e all elements in the given string is valid such that only the string is valid and we return the True for that 
                                            # here if all elements are poped from the stack ==> it mean's given string is valid ==> so return True ==> why ? all elements are removed the len of stack is '0' right 
print(valid_parenthesis("[})"))


# here in the line number of 57 ==> if top element of stack is matched with the mappings that means we it's a valid part of brackets in string 
# so at that point ==> in theory part what we do after the part of brackets is valid then return True and pop it out na 


# but here we did the if part of string is invalid ==> we immediately return the false and pop element from the stack so the oopening bracket will be lost at that time and if again the opening bracket is entered it will directly added into the stack so worries.
