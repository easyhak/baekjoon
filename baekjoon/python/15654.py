# N과 M(5), 15654.py
# 출처: 
# 알고리즘 분류: 백트래킹

from itertools import permutations
n, m = map(int,input().split())
arr = list(map(int,input().split()))
per =  list(permutations(arr,m))
per.sort()
for i in per:
    print(*i)
