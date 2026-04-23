
# “Given an integer array and a target value, find three numbers such that their sum is closest to the target. Return the sum.”

# 🔍 Example
# Input: nums = [-1, 2, 1, -4], target = 1
# Output: 2

# Explanation:
# Closest sum is (-1 + 2 + 1 = 2)

# brute force approach 

def three_sum_closest(arr,target):
    arr.sort()
    n = len(arr)
    closest = float('inf')
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                total = arr[i] + arr[j] + arr[k]
                
                if abs(total - target) < abs(total - closest):
                    closest = total 
    return closest
print(three_sum_closest([-1,2,1,-1],1))             #2

# optimal solution approach 

def three_sum_closest(arr,target):

    n = len(arr)
    closest = float('inf')
    arr.sort()

    for i in range(n-2):
        l = i + 1
        r = n - 1

        total = arr[i]+arr[l]+arr[r]

        if abs(target - total) < abs(target - closest):
            closest = total

        if total < target:
            l+=1

        elif total > target:
            r -= 1

        else:
            return total            # when exact match i.e when total = closest i think not exactly

    return closest

print(three_sum_closest([-1,2,1,-4],1))             #2

