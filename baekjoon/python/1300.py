# k 번째 수 / 1300.py
# 알고리즘 분류: 이분 탐색, 매개 변수 탐색
n = int(input())
k = int(input())
left = 1
right = k
while(left < right):
	mid = (right+left) // 2
	count = 0
	for i in range(1,n+1):
		count += min(mid // i, n)
	if k > count:
		left = mid + 1
	else:
		right = mid
print(left)