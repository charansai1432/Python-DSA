# Problem: Sort Colors (Dutch National Flag)
# 🧾 Interview-style question

# “Given an array with values only 0, 1, 2, sort it in-place without using sort().”




# # brute force approach 

def sort_colours(arr):
    arr.sort()
    return arr
print(sort_colours([1,1,0,0,2,2]))


# optimal solution is using the 3 pointer approach 

# 🔥 Key Idea

# Step 1: What is the problem REALLY asking?

# You are given:

# [2,0,2,1,1,0]

# You need:

# [0,0,1,1,2,2]

# 👉 But you cannot sort directly
# 👉 You must do it in one pass, in-place

# 🔥 Step 2: Think in terms of GROUPS (not numbers)

# We want:

# All 0s → left side  
# All 1s → middle  
# All 2s → right side
# 🧠 Step 3: Divide array into regions

# Imagine splitting array into parts:

# [ 0 zone | 1 zone | unknown | 2 zone ]

# At the beginning:

# [ unknown unknown unknown unknown unknown unknown ]

# 👉 Nothing is sorted yet

# 🔥 Step 4: What are the pointers?
# 🟢 low → start of 1 zone

# 👉 Everything before low is already 0

# 🟡 mid → current element

# 👉 This is the element we are checking

# 🔴 high → end of 2 zone

# 👉 Everything after high is already 2

# 🧠 Visual Representation
# Index:   0   1   2   3   4   5
# Array:  [2,  0,  2,  1,  1,  0]

# low = 0
# mid = 0
# high = 5

### optimal solution ###

def sort_colors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
    return arr

print(sort_colors([1,1,3,2,2,0,0]))