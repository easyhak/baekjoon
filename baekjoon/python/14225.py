# 부분수열의 합 / 14225.py
# 알고리즘 분류: 브루트포스 알고리즘
import heapq
from itertools import combinations

n=int(input())
arr=list(map(int,input().split()))
heap=[]
for i in range(1,n+1):
    for x in combinations(arr,i):
        heapq.heappush(heap,sum(x))

l=len(heap)
x=0; ans=heap[-1]+1; t=0;i=1
while heap:
    x=heapq.heappop(heap)
    if t==x:
        continue
    t=x
    if i!=x:
        ans=i
        break
    i=i+1

print(ans)