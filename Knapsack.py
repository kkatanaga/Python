items = 3
capacity = 5
values = (1,2,3)
weight = (4,5,1)

def knapsack(cap, weights : list, values : list, n):
    max_list = []
    index = 0
    for i, w1 in enumerate(weights):
        if w1 <= cap:
            max_list.append(values[i])
            index += 1
            if w1 < cap:
                for j in range(i + 1, n):
                    if max_list[index] + weights[j] <= cap:
                        max_list.append(values[j])
                        index += 1
    max = 0
    for m in max_list:
        if max < m:
            max = m
    return max

max_value = knapsack(capacity, weight, values, items)
print(max_value)