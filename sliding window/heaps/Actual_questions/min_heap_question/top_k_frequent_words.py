

def top_k_frequent_words(words,k):
    from collections import Counter 
    freq = Counter(words)
    print(freq)
    heap = []
    
    import heapq 
    for word in freq:
        heapq.heappush(heap,(freq[word],word))
        
        if len(heap) > k:
            heapq.heappop(heap)
            
    result = []
    while heap:
        freq,word = heapq.heappop(heap)
        result.append(word)
    return result
print(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"],2))