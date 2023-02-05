from functools import reduce

def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    count_ngtv = 0
    large_ngtv = -999999999999
    
    xs_new = [num for num in xs if num != 0]

    for x in xs_new:
        if x < 0:
            count_ngtv += 1
            large_ngtv = max(large_ngtv, x)
    
    odd = count_ngtv % 2
    
    if odd == 0:
        return str(reduce(lambda x, y: x * y, xs_new))
    

    if len(xs_new) == 1:
        if xs_new[0] < 0:
            return str(0)
            
        return str(xs_new[0])
    
    xs_new.remove(large_ngtv)
    
    return str(reduce(lambda x, y: x * y, xs_new))

max_power = solution([-2, -3, 4, -5])
print(max_power)