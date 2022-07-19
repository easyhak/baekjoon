# 섬의 개수 / 4963.py
# 문제 출처: ICPC > Regionals > Asia Pacific > Japan > Japan Domestic Contest > 2009 Japan Domestic Contest B번
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
from collections import deque
import sys; input = sys.stdin.readline
def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    while queue:
        x, y = queue.popleft()
        matrix[x][y] = 0
        for p, q in move:
            dx = x + p
            dy = y + q
            if 0<=dx<m and 0<=dy<n and matrix[dx][dy] == 1:
                matrix[dx][dy] = 0
                queue.append((dx,dy))
move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    matrix = []
    for i in range(m): 
        matrix.append(list(map(int,input().split())))
    cnt = 0
    
    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 1 :
                cnt += 1
                bfs(a,b)        
    print(cnt)