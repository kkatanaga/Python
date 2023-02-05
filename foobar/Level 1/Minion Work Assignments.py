def solution(data, n): 
    assignments = list(data)
    
    for x in range(len(assignments)):
        for task in assignments:
            if assignments.count(task) > n:
                while task in assignments:
                    assignments.remove(task)
                break
        
    return assignments

assigned = solution([1, 1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
print(assigned)