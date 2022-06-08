# 연구소 / 14502.py
# 출처: 
# 알고리즘 분류: 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색
from collections import deque; import sys; import copy
input=sys.stdin.readline
n,m=map(int,input().split())
queue= deque([]); matrix=[]; zeros=[]; ans=100; one_count=0 # 초기화
for i in range(n):
    matrix.append(list(map(int,input().split())))
    for j in range(m):
        if matrix[i][j]==2:
            queue.append((i,j)) # 2인 값 queue에 넣어주기
        elif matrix[i][j]==0:
            zeros.append((i,j)) # zero값 넣기
        else:
            one_count+=1
one_count=one_count+3; two_count=len(queue) 
cors=[(-1,0),(1,0),(0,1),(0,-1)]
def combinations(arr,r): # 조합을 이용햇 벽을 세울 0 세개의 값 얻기
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]]+next
def bfs(graph,queue): # bfs를 통해 답 찾기
    cnt=0; global ans
    while queue:
        x,y=queue.popleft()
        for a,b in cors:
            dx=x+a
            dy=y+b
            if 0<=dx<n and 0<=dy<m and graph[dx][dy]==0: # 범위에 맞고 값이 0이면
                cnt+=1
                graph[dx][dy]=2
                queue.append((dx,dy))
    ans = min(ans,cnt)
for i in combinations(zeros,3):
    graph=copy.deepcopy(matrix) 
    # deepcopy를 꼭 해줘야함 graph=matrix[:] 이렇게 하면 안됨
    q=copy.deepcopy(queue)
    # 이것도 deepcopy
    for x,y in i:
        graph[x][y]=1
    bfs(graph,q)
# 안전지대의 크기 = 전체 크기 - 1의 크기 - 2의 크기(최솟값+원래 2의 크기)
print(n*m-one_count-(ans+two_count)) 