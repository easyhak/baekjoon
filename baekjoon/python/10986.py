# 나머지 합 / 10986.py
# 알고리즘 분류: 수학, 누적 합

from collections import Counter
from math import comb

n,m=map(int,input().split())
arr=list(map(int,input().split()))
prefix_sum=[0]
for i in arr:
    prefix_sum.append((prefix_sum[-1]+i)%m)
ans=0
c=Counter(prefix_sum)
c[0]=c[0]-1
ans+=c[0]
for i in c.keys():
    ans+=comb(c[i],2)
print(ans)