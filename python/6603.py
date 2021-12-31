# 로또, 6603.py
# 출처: 
# 알고리즘 분류: 수학, 조합론, 백트래킹, 재귀
from itertools import combinations
while True:
    numbers = list(map(int,input().split()))
    arr = numbers[1:]
    numbers.sort()
    if numbers[0] == 0:
        break
    
    ans = combinations(arr,6)
    for i in ans:
        print(*i)
    print()