# 수들의 합 2 / 2003.py
# 출처: 
# 알고리즘 분류: 두 포인터

import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int, input().split()))
p = [i+1 for i in range(n)]

sum_value = 0
prefix_sum = [0]
for i in arr:
	sum_value+=i
	prefix_sum.append(sum_value)
count = 0
for i in range(1,n+1):
	for j in range(i,n+1):
		
		if m < prefix_sum[j]-prefix_sum[i-1]:
			continue
		elif m == prefix_sum[j]-prefix_sum[i-1]:
			count += 1
print(count)
