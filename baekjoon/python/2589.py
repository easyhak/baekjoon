# 출처: Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2005 > 초등부 3번
# 알고리즘 분류: 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

from collections import deque

n, m = map(int,input().split())
matrix = []
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    matrix.append(list(input()))


def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited = [[0]*m for _ in range(n)] # reset visit
    visited[i][j] = 1
    cnt = 0
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = dx[k]+x; ny = dy[k]+y
            if 0<=nx<n and 0<= ny<m and not visited[nx][ny] and matrix[nx][ny] == "L":
                visited[nx][ny] = visited[x][y] + 1 
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx,ny))
    return cnt - 1 

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "L":
            answer = max(answer, bfs(i,j))
print(answer)


