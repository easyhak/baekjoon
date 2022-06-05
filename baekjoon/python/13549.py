# 숨바꼭질 3 / 13549.py
# 출처: 
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라, 0-1 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
queue.append(n)

def bfs():
    while queue:
        x = queue.popleft()
        if x == k:
            print(ans[x])
            break
        if 0<= x*2 <= 100000 and not visited[x*2]:
            visited[x*2]= True 
            ans[x*2] = ans[x]
            queue.append(x*2)
        for nx in (x-1, x + 1):
            if 0<= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                ans[nx] = ans[x]+1
                queue.append(nx)
ans = [0] * 100001
visited = [False] * 100001

bfs()