# 스타트와 링크, 14889.py
# 알고리즘 분류: 백트래킹, 브루트포스 알고리즘
from itertools import combinations
from itertools import permutations
import sys; input=sys.stdin.readline
n=int(input())
arr=[i for i in range(n)]
comb=list(combinations(arr,n//2))
players=[]
for i in range(n):
    players.append(list(map(int,input().split())))
ans=2000
for x in comb:
    start,link=0,0
    for a,b in list(permutations(x,2)):
        start+=players[a][b]
    for a,b in list(permutations(list(set(arr)-set(x)),2)):
        link+=players[a][b]
    ans=min(abs(start-link),ans)
print(ans)