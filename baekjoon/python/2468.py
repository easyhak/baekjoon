# 안전 영역 / 2468.py
# 출처: Olympiad > 한국정보올림피아드 > KOI 2010 > 초등부 2번
# 알고리즘 분류: 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
from collections import deque
move = [(-1,0),(1, 0),(0, -1),(0, 1)]
def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    
    while queue:
        x, y = queue.popleft()
        for p, q in move:
            dx, dy = x + p, y + q
            if 0<= dx < n and 0<= dy < n and area[dx][dy] == 1:
                area[dx][dy] = 0
                queue.append([dx, dy])

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

m = 0
for i in matrix:
    m = max(i)
ans = 0
for i in range(m+1):
    area = [[0]*n for _ in range(n)]
    for x in  range(n):
        for y in  range(n):
            if matrix[x][y] > i:
                area[x][y] = 1
    cnt = 0
    for x in range(n):
        for y in range(n):
            if area[x][y] == 1:
                cnt += 1
                area[x][y] = 0
                bfs(x, y)
    ans = max(ans, cnt)
print(ans)