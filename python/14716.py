# 현수막 / 14716.py
# 출처: University > 충남대학교 > 생각하는 프로그래밍 대회  A번
# 알고리즘 분류: 그래프 이론,그래프 탐색,너비 우선 탐색,깊이 우선 탐색

import sys
from collections import deque

m, n = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
    
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b]=0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0<= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return 1
result = []
for i in range(m):
    for j in range(n):
            if graph[i][j] == 1:
                result.append(bfs(i,j))

print(len(result))
