from sys import exit

def ada_sort(fabrics) :
    return sorted(fabrics, key=lambda x: x[0])

def charles_sort(fabrics) :
    return sorted(fabrics, key=lambda x: x[1])

T, N = 0, 0

T = input()
if 0 == int(T):
    exit("")

fabrics = []

for i in range(int(T)):
    count = 0
    N = input()
    if int(N) == 0:
        exit("")
    
    for j in range(int(N)):
        fabric = input().split()
        try:
            int_test = int(fabric[1])
            int_test = int(fabric[2])
        except ValueError:
            exit("")
        
        fabrics.append(fabric)
    ada_sorted = ada_sort(fabrics)
    charles_sorted = charles_sort(fabrics)
    
    compare = [i for i, j in zip(ada_sorted, charles_sorted) if i == j]
    count = len(compare)

    print(f"Case #{i + 1}: {count}")
    fabrics.clear()

