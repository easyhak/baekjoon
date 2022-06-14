# 숫자 이어 붙이기 / 24955.py
# 출처: Contest > 쇼미더코드: 원티드 주관 코딩테스트 대회 > 2022년 1회차 B번 
# 알고리즘 분류: 수학, 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색 ,최소 공통 조상
from collections import deque
import sys; input=sys.stdin.readline
n, q = map(int, input().rstrip().split())
arr = [""]+input().rstrip().split() # index 1서부터 시작
road={}
for i in range(n+1):
    road[i]=[] 
for i in range(n-1):
    a,b=map(int,input().split())
    road[a].append(b); road[b].append(a) # dic-list로 연결
for i in range(q):
    visited=[False]*(n+1)
    queue=deque()
    x,y=map(int,input().split())
    visited[x]=True
    queue.append((x,arr[x]))
    while queue:
        c,d=queue.popleft()   
        if c==y:
            print(int(d)%1000000007)
            break
        for adj in road[c]:
            if not visited[adj]:
                visited[adj]=True
                queue.append((adj,d+arr[adj]))