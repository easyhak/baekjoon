# 알고리즘 수업 - 깊이 우선 탐색 1 / 24779.py
# 알고리즘 분류:그래프 이론, 그래프 탐색, 정렬, 깊이 우선 탐색
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
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
def dfs(r):
    global count
    visited[r]=count
    for i in edge[r]:
        if visited[i]==0:
            count+=1
            dfs(i)
dfs(r)
for i in range(1,n+1):
    print(visited[i])