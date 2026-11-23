# Identify the pattern
# Let's identify the clues:
# 1. We need to rearrange characters to satisfy a condition.
# 2. We need to prioritize characters that occur most frequently.
# 3. We must avoid selecting the same character in consecutive positions.
# This suggests Greedy + Max Heap.

# The Max Heap helps us select the character with the highest remaining frequency.

# # The Greedy strategy helps us place the most frequent available character while avoiding adjacent duplicates.

# #  max_heap + greedy algo 

def reorganize_string(s):
    
    
    pass 
    
    
print(reorganize_string("aab")) # aba
print(reorganize_string("aba")) # ""