# Whenever a problem repeatedly asks you to combine the two smallest available values, calculate their combined cost, and put the result back, think of Greedy + Min Heap.

# Brute force approach 

cards = [4, 3, 2, 6]
def combine_cards_or_numbers_to_minimum_cost(cards):
    min_cost = 0 
    while len(cards) > 1:
        first_small_number = min(cards)
        cards.remove(first_small_number)
        
        second_small_number = min(cards)
        cards.remove(second_small_number)

        min_cost += first_small_number + second_small_number
        
        new_number = first_small_number + second_small_number 
        
        cards.append(new_number)
    return min_cost
print(combine_cards_or_numbers_to_minimum_cost(cards))

#  optimal solution 
cards = [4, 3, 2, 6]
def combine_cards_or_numbers_to_min_cost(cards):
    min_cost = 0
    import heapq 
    heapq.heapify(cards)
    while len(cards) > 1:
        first_small_number = heapq.heappop(cards)
        second_small_number = heapq.heappop(cards)
        
        min_cost += first_small_number + second_small_number 
        
        new_number = first_small_number + second_small_number
        
        heapq.heappush(cards,new_number)
        
    return min_cost
print(combine_cards_or_numbers_to_min_cost(cards))
        