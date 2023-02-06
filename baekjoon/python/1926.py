# 그림, 1926.py
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())

graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,input().split())))
pic_cnt = 0; M = 0

for i in range(n):
    for j in range(m):
        queue = deque()
        
        if graph[i][j] == 1 and visited[i][j] == False:
            pic_cnt += 1; tmp = 1
            visited[i][j] = True
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]      
                    if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        tmp += 1
                        queue.append((nx,ny))
            M = max(M, tmp)

print(pic_cnt)
print(M)