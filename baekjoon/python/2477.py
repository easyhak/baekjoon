# 참외밭 / 2477.py
# 출처: Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2010 > 중등부 2번
# 알고리즘 분류: 구현, 기하학
import sys; input = sys.stdin.readline
k = int(input())
arr=[]
x, y, maxw, maxh =0,0,0,0
for i in range(6):
    arr.append(list(map(int, input().split())))
for a,b in arr:
    if a == 1 or a == 2:
        if maxw < b:
            maxw = b
    else:
        if maxh < b:
            maxh = b
for i in range(6):
    if(arr[i%6][0]==arr[(i+2)%6][0] and arr[(i+1)%6][0]==arr[(i+3)%6][0]):
        x=arr[(i+1)%6][1]
        y=arr[(i+2)%6][1]
print(((maxh*maxw)-(x*y))*k)