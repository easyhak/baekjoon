# 알고리즘 수업 - 너비 우선 탐색 1 / 24444.py
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
import sys; input = sys.stdin.readline

n,m,r=map(int,input().split())
edge= [[] for _ in range(n + 1)]
visited=[0]*(n+1)

for _ in range(1, m + 1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
for i in range(1,n+1):
    edge[i].sort()
count=1
queue=deque()
def bfs(r):
    global count
    visited[r]=count
    queue.append(r)
    while queue:
        x=queue.popleft()
        for i in edge[x]:
            if visited[i]==0:
                count+=1
                visited[i]=count
                queue.append(i)
bfs(r)
for i in range(1,n+1):
    print(visited[i])