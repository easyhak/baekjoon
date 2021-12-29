# 연결요소의 개수, 11724.py
# 출처: 
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node2].append(node1)
    graph[node1].append(node2)
def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i,visited)
        cnt+=1
print(cnt)