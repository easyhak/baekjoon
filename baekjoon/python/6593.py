# 상범 빌딩 / 6593.py
# 출처: Contest > University of Ulm Local Contest > University of Ulm Local Contest 1997 D번
# 알고리즘 분류: 그래프 이론,그래프 탐색, 너비 우선 탐색

from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(x, y, z):
    queue.append([x, y, z])
    visited[x][y][z] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if matrix[nx][ny][nz] == 'E':
                    print(f"Escaped in {visited[x][y][z]} minute(s).")
                    return
                if matrix[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    queue.append([nx, ny, nz])
    print("Trapped!")

while True:
    l,r,c = map(int, input().split())
    if l == 0 and r == 0 and c ==0:
        break
    matrix = [[[]*c for _ in range(r)] for _ in range(l)]
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    queue = deque()
    for i in range(l):
        temp = []
        for x in range(r):
            temp.append(list(map(str, input().strip())))
        matrix[i] = temp
        input() # 엔터 입력
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if matrix[i][j][k] == 'S':
                    bfs(i, j, k)
