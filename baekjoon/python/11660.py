# 구간 합 구하기 5 / 11660.py
# 알고리즘 분류: 다이나믹 프로그래밍, 누적 합
import sys; input=sys.stdin.readline
n, m = map(int, input().split())
table=[]
for i in range(n):
    table.append(list(map(int,input().split())))
prefix_sum=[]
for i in table:
    temp_sum=[0]
    for j in range(len(i)):
        temp_sum.append(temp_sum[-1]+i[j])
    prefix_sum.append(temp_sum)
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    ans=0
    for i in range(x1,x2+1):
        ans+=prefix_sum[i][y2]-prefix_sum[i][y1]+table[i][y2]
    print(ans)