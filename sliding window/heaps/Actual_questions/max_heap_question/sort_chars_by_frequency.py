def sort_chars_by_frequecy(s):
    import heapq 
    heap = []
    result = ""
    from collections import Counter 
    freq = Counter(s)
    for ch in freq:
        heapq.heappush(heap,(-freq[ch],ch))
        
    while heap:
        count ,ch = heapq.heappop(heap)
        result += ch * -(count)
    return result 
print(sort_chars_by_frequecy("aabbb"))          # bbbaa