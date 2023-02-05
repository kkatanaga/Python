from itertools import combinations

def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    xs_new = [num for num in xs if num != 0]

    if len(xs_new) == 1:
        if xs_new[0] < 0:
            return str(0)
            
        return str(xs_new[0])

    result = 0
    
    for i in range(len(xs_new) + 1):
        comb = list(combinations(xs_new, i))
        for i in comb:
            prod = 1
            for j in i:
                prod *= int(j)
            result = max(result, prod)
    
    return str(result)

max_power = solution([0, -4, 4])
print(max_power)