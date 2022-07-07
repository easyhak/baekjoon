# 뱀과 사다리 게임 / 16928.py
# 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
from collections import defaultdict
import sys; input = sys.stdin.readline
n, m = map(int,input().split())
matrix = [0]*101
ladder_snake = defaultdict(int)
move = [1,2,3,4,5,6]
for i in range(n+m):
	x, y = map(int,input().split())
	ladder_snake[x] = y
def bfs():
	queue = deque()
	queue.append(1)
	while queue:
		x = queue.popleft()
		if x == 100:
			print(matrix[100])
		for i in move:
			dx = x + i
			if 1<= dx < 101 and not matrix[dx]:
				if ladder_snake[dx]:
					dx = ladder_snake[dx]
				if not matrix[dx]:
					
					matrix[dx]=  matrix[x]+1
					queue.append(dx)
				
bfs()
					