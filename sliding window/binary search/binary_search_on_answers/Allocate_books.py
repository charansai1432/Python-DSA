
# this is the question
# the actual question says that the minimum pages to allocate a student such that no student can feel burden 


# here in the array book = [ pages1,pages2,pages3]

# optimal solution 

def Allocate_books(pages,S):
    
    def possible(max_pages_per_student):
        
        cur_pages = 0
        student = 1 
        for page in pages:
            if cur_pages + page > max_pages_per_student:
                
                student += 1
                cur_pages = page
            else:
                cur_pages += page
        return student <= S
    
    l = max(pages)          # a student can able to read only maximum of this no.of  pages
    r = sum(pages)                  # a another student can able to read the entire book which gives the search space for this one
    answer = r
    while l <= r:
        mid = l + (r-l)//2
        if possible(mid):
            answer = mid
            r = mid - 1             # the minimum no. of pages such that no one student can feel burden for this 
        else:
            l  = mid + 1
    return answer
print(Allocate_books())