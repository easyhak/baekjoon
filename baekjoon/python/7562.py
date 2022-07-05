# 7562.py / 나이트의 이동
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque

move = [(1,2), (2,1) , (-1,-2), (-2,-1), (1,-2), (2,-1), (-1,2), (-2,1)]
t = int(input())

for i in range(t):
    l = int(input())
    present_x, present_y = map(int,input().split())
    goal_x, goal_y = map(int,input().split())

    matrix = [ [0]*l for _ in range(l)]
    visited = [ [0]*l for _ in range(l)]
    queue = deque()
    queue.append([present_x, present_y])
    visited[present_x][present_y] = 1
    while queue:
        x,y = queue.popleft()
        if x == goal_x and y == goal_y:
            print(matrix[x][y])
            break
        for dx, dy in move:
            kx, ky = x + dx, y + dy
            if 0<=kx<l and 0<=ky<l and not visited[kx][ky]:
                visited[kx][ky] = 1
                matrix[kx][ky] = matrix[x][y]+1
                queue.append([kx,ky])