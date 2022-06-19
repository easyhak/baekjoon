# 회의실 배정, 1931.py
# 알고리즘 분류: 그리디 알고리즘, 정렬
import sys; input=sys.stdin.readline
n=int(input())
council=[]
start=[];end=[]
for i in range(n):
    council.append(list(map(int, input().split())))
   
council.sort(key=lambda a: (a[1],a[0])) # 끝나는 시간, 시작 시간 순으로 정렬
start=[i[0] for i in council]
end=[i[1] for i in council]

ans=[0];k=0 # 0번 먼저 탐색
# 그리디 알고리즘
for i in range(1,n): 
    if start[i]>=end[k]:
        ans.append(i)
        k=i # 끝나는 시간 index 변경
print(len(ans))