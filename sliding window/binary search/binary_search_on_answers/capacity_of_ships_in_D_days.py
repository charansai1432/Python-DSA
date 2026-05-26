






# optimal solution 

def capacity_of_ships_in_D_days(weights,D):
    def possible(ship_capacity):
        cur_load = 0
        days_used = 1
        for weight in weights:
            if cur_load + weight > ship_capacity:
                days_used += 1
                cur_load = weight
            else:
                cur_load += weight
        return days_used <= D
    l = max(weights)
    r = sum(weights)
    answer = r
    while l <= r:
        mid = l + (r-l) // 2
        if possible(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer
print(capacity_of_ships_in_D_days([1,2,3,4,5,6,7,8,9,10],5))