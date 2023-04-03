# 영역 구하기 / 2583.py
# 출처: Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 고등부 2번
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
from collections import deque

# 입력 및 초기화
m, n, k = map(int,input().split())
arr = [[0]*n for _ in range(m)]
for i in range(k):
    a, b, c, d = map(int,input().split())
    for x in range(a,c):
        for y in range(b, d):
            arr[y][x]=1

nx = [0,0,1,-1]
ny = [1,-1,0,0]
ans = 0
area_list = []
queue = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            area = 1
            queue.append((i,j))
            arr[i][j]=1
            ans += 1 # 구분된 개수 증가
            # bfs
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    dx = x+nx[k]; dy = y+ny[k]
                    if 0<=dx<m and  0<=dy<n and arr[dx][dy] != 1:
                        area+=1
                        arr[dx][dy]=1
                        queue.append((dx,dy))
            area_list.append(area)
print(ans)
print(*sorted(area_list))