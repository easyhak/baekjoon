# 쿼드트리/1992.py
# 알고리즘 분류: 분할 정복, 재귀
from collections import deque

n=int(input())
matrix=[]
for i in range(n):
	matrix.append(list(input().rstrip()))
def solution(x,y,n):
	color=matrix[x][y]
	for i in range(x,x+n):
		for j in range(y,y+n):
			if color!=matrix[i][j]:
				print('(',end='')
				solution(x,y,n//2)
				solution(x,y+n//2,n//2)
				solution(x+n//2,y,n//2)
				solution(x+n//2,y+n//2,n//2)
				print(')',end='')
				return
	print(color,end='')
	return
solution(0,0,n)