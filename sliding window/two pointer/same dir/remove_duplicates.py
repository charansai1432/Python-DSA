#brute force approach

def remove_duplicates(arr):
    
    uniq = set()
    dup = []
    for num in arr:
        if num in uniq:
            dup.append(num)
            
        uniq.add(num)
    return uniq
print(remove_duplicates([1,1,2,3,4,5]))

