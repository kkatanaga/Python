def solution(x, y):
    sum = 0

    for i in range(1, x + 1):
        sum += i

    for j in range(x, x + y - 1):
        sum += j

    return str(sum)