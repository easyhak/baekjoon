# 스타트링크 / 5014.py
# 출처: ICPC > Regionals > Europe > Northwestern European Regional Contest > Nordic Collegiate Programming Contest > NCPC 2011 D번
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0]*(f+1)
move = [u,-d]
queue = deque()
queue.append(s)
flag = False
while queue:
    x = queue.popleft()
    if x == g:
        flag = True
        break
    for i in move:
        dx = i + x
        if 0< dx <= f and not visited[dx] and i != 0:
            visited[dx]=visited[x]+1
            queue.append(dx)
print(visited[g] if flag else "use the stairs")