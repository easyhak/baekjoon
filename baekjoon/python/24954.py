# 24954.py / 물약 구매
# 출처: Contest > 쇼미더코드: 원티드 주관 코딩테스트 대회 > 2022년 1회차 A번
# 알고리즘 분류: 구현, 브루트포스 알고리즘
from itertools import permutations
import sys; input=sys.stdin.readline
n=int(input())
sale=[]
val=list(map(int,input().split()))
index={}
for i in range(len(val)):
    index[val[i]]=i

for i in range(n):
    p=int(input())
    temlist=[]
    for j in range(p):
        temlist.append((list(map(int,input().split()))))
    sale.append(temlist)

ans=100001
for i in permutations(val,n):
    s=0
    tempval=val[:]
    for j in i:
        for x,y in sale[index[j]]:
            tempval[x-1] = 1 if tempval[x-1]-y<=1 else tempval[x-1]-y
        s+=tempval[index[j]]
    ans=min(s,ans)
print(ans)