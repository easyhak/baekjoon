# 평범한 배낭 / 12865.py
# 알고리즘 분류: 다이나믹 프로그래밍, 배낭 문제
import sys; input=sys.stdin.readline
n,k=map(int,input().split())
record=[0]*(k+1)
for i in range(n):
    w,v=map(int,input().split())
    if k<w: 
        continue
    for j in range(k,0,-1): # 역순으로 해줘야함// 반례: /3 5/4 2/3 4/1 5/
        if record[j]!=0 and j+w<=k:
            record[j+w]=max(record[j+w],record[j]+v)
    record[w]=v
print(max(record))