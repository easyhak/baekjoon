# 어두운 건 무서워 / 16507.py
# 출처: University > 충남대학교 > 제2회 생각하는 프로그래밍 대회 E번
# 알고리즘 분류: 누적 합

import sys
input = sys.stdin.readline
r, c, q = map(int, input().split())
pic = []
for i in range(r):
	pic.append(list(map(int, input().split())))
prefix_sum = [[0]for _ in range(r)]
for i in range(r):
	value = 0
	for j in range(c):
		value += pic[i][j]
		prefix_sum[i].append(value)

for _ in range(q):
	sum = 0
	r1,c1,r2,c2 = map(int, input().split())
	for i in range(r1-1, r2):
		sum+=prefix_sum[i][c2]-prefix_sum[i][c1-1]
	print(sum//((r2-r1+1)*(c2-c1+1)))