
# this is the question where in the array every element is appeared twice but only one element is appeared once return that element(only once appeared)
# and return its index 

# brute force approach 

def single_element_in_sorted_array(arr):
    from collections import Counter
    freq = Counter(arr)
    for num in arr:
        if freq[num] == 1:
            return num 
#     return -1
# print(single_element_in_sorted_array([1,1,2,2,3,3,4]))
# print(single_element_in_sorted_array([1,1,2,2,3,3]))
# print(single_element_in_sorted_array([0,0,0,0]))
# print(single_element_in_sorted_array([]))


# optimal solution approach 

# to solve this quesiton in the optimal manner see here now 
# [0,1,2,3,4,5,6] ==> index postions
# [1,1,2,2,3,3,4] ==> Actual elements

#  here the every element starting index position is at index of even numbers only i.e [index -> number] ==>   [0 -> 1 , 2 -> 2 , 4 -> 3 ]

#  I.E when ever the even index breaks ==> there only the single element is found and at index should be the odd index.

def single_element_in_sorted_array(arr):
    n = len(arr)
    l = 0
    r = n - 1 
    
    if len(arr) == 0:
        return -1 
    
    while l < r:            # here in the while condition (DON'T KEEP THE L <= R) because in the question every element is appeared twice if we keep the l <= r again the pointer can compare the same element twice which cause the problem and also cause the index out of range issue
        mid = l + (r - l )//2
        
        if mid % 2 == 1:            # here if mid(index position) is odd that's where the even -> odd breaks and single element could be found

            mid -= 1                # and we shrink the mid -= 1 ==> why ? ==> to verify ===> whether it's correct or wrong ....that means 
                                            # if mid = 2 assume the now mid position is even then a even pair is found 
                                            
        if arr[mid] == arr[mid+1]:          # now if now mid,mid + 1 is same i.e [1,1,2,2,3] here arr[mid] == arr[mid+1] ==> [2,2] ==> even pair then may if be l = mid + 2 only which gives the single element
            l = mid + 2                 # [       3,   3,    4]  
                                        # [     ,mid,mid+1      ]  what means if we move the l = mid + 1 it still points to the same number which causes the more time so simple move the left pointer '2' steps forward
                                         
        elif arr[mid] != arr[mid+1]:            # if mid != mid+1 then we found the single element and here the cur_pos of mid which gives the answer in the sences r =  mid 
            r = mid                                     # in this position the single element  is found 
            
    return arr[r]                           # return that single element or its index according to the question 
print(single_element_in_sorted_array([1,1,2,2,3,3,4]))
# print(single_element_in_sorted_array([1,1,2,2,3,3]))
# print(single_element_in_sorted_array([0,0,0,0]))
# print(single_element_in_sorted_array([]))
