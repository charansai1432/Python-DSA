
# “Given an integer array and a target value, find three numbers such that their sum is closest_sum to the target. Return the sum.”

# 🔍 Example
# Input: nums = [-1, 2, 1, -4], target = 1
# Output: 2

# Explanation:
# closest_sum  is (-1 + 2 + 1 = 2)

# brute force approach 

def three_sum_closest_sum(arr,target):
    arr.sort()
    n = len(arr)
    closest_sum = float('inf')              # the closest_sum is float('inf') i.e from a big value to small_value 
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                total = arr[i] + arr[j] + arr[k]
                
                if abs(total - target) < abs(total - closest_sum):          # remember this condition 
                    closest_sum = total 
    return closest_sum
print(three_sum_closest_sum([-1,2,1,-1],1))             #2

# optimal solution approach 

def three_sum_closest_sum(arr,target):

    n = len(arr)
    closest_sum = float('inf')
    arr.sort()

    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:            # to remove the duplicates 
            continue
        
        l = i + 1
        r = n - 1
        while l < r:
            
            total = arr[i]+arr[l]+arr[r]

            if abs(target - total) < abs(target - closest_sum):
                
                closest_sum = total

            if total < target:
                l+=1

            elif total > target:
                r -= 1

            else:
                return total            # when exact match i.e when total = closest_sum i think not exactly

    return closest_sum

print(three_sum_closest_sum([-1,2,1,-4],1))             #2

