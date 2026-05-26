


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
    l = max(pages)
    r = sum(pages)
    answer = r
    while l <= r:
        mid = l + (r-l)//2
        if possible(mid):
            answer = mid
            r = mid - 1
        else:
            l  = mid + 1
    return answer
print(Allocate_books())