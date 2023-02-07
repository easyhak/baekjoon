# 빙산 / 2573.py
# 출처: Olympiad > 한국정보올림피아드 > KOI 2006 > 초등부 2번
# 알고리즘 분류: 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque
import sys

input = sys.stdin.readline

dx = [1,-1,0,0]; dy = [0,0,1,-1]           
n, m = map(int, input().split())
ans = 0

# 빙산의 개수 구하기
def bfs(graph: list):
    cnt = 0
    visited = [[False]*m for _ in range(n)]

    # 모두다 0 인지 확인하기 빙하가 다 녹았으면 끝
    if len(set(sum(graph, []))) == 1: 
        return -1

    # bfs
    for i in range(n):
        for j in range(m):
            queue = deque()
            if graph[i][j] != 0 and visited[i][j] == False: 
                cnt += 1
                visited[i][j] = True
                queue.append((i,j))
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k] 
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and graph[nx][ny]!=0:
                            visited[nx][ny] = True
                            queue.append((nx,ny))
    return cnt

graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))


while(True):
    # 모두다 0이면 break
    status = bfs(graph)
    if status == -1: # 얼음이 다 녹은 상황
        ans = 0
        break
    if status >= 2:
        break
    ans += 1
    water = [[0]*m for _ in range(n)]

    # 얼음 녹이기
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if graph[i][j] != 0:
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                        water[i][j]+=1 # 주변의 물을 저장
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j]-water[i][j]) # 빼기, 뺀 값이 0보다 작으면 0으로 설정


print(ans)