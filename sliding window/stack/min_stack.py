
# brute force approach 

def min_stack():
    
    
    pass
    
print(min_stack())








# here the actual question ==> to return the minimum element in a stack 
# and the min_element should be written in the O(1) time complexity 
# we can think intially => we can directly use the min() function but it cause the time complexity of O(N)

# so in stack we use the technique ===> for every iteration we caluculate the min_value 

# Here the stack not only store the value 
# but also store the min_value for every iteration of push 

# stack looks like this 


# | ('0' postion ,'1' position ) |
# | (actual_value , min_val_till_now) |

# | (val,min_val_till_now) |
# | (val,min_val_till_now) |
# | (val,min_val_till_now) |

# optimal solution 
class min_stack:
    def __init__(self):         # self = current calling object 
        self.stack = []             # here we intialize a stack 
        
    def push(self,val): 
        
        if not self.stack:      # if stack is empty append the values 
            self.stack.append((val,val))                # at 1st iteration the min_val is the min_val of the same element only 
        else:
            cur_min = min(val,self.stack[-1][1])        # the min_element is present at position in stack [-1][1] i.e every time a val passed the last element comes first a/c to stack i.e top element[-1][1] ==> which gives the min_element
            self.stack.append((val,cur_min))            # which calculates the min_element till now
    
    def top(self):
        return self.stack[-1][0]            # top most value present at [0] postion at [-1] last postion 
    
    def pop(self):
        return self.stack.pop()     # deletes the last element in stack 
    
    def min_element(self):
        return self.stack[-1][1]            # here the min_element is present in [1] positoin of [-1] of top element in stack
    
    def print(self):
        return self.stack               # print the total stack to see 

s1 = min_stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)

print(s1.pop())
print(s1.top())

print(s1.print())

print(s1.min_element())
