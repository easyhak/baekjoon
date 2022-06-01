# 어린왕자 / 1004.py
# 출처: 
# 알고리즘 분류: 기하학
import sys; import math; input = sys.stdin.readline
t=int(input())
for _ in range(t):     
    cnt=0
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    for _ in range(n):
        cx,cy,r=map(int,input().split())
        if(math.pow(x1-cx,2)+math.pow(y1-cy,2)<=math.pow(r,2)) != (math.pow(x2-cx,2)+math.pow(y2-cy,2)<=math.pow(r,2)):
            cnt+=1
    print(cnt)