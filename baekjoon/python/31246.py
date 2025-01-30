# 모바일 광고 입찰 / 31246.py
# 알고리즘 분류: 정렬

n, k = map(int, input().split())
val = []
for x in range(n):
    a, b = map(int,input().split())
    val.append((a, b))

val.sort(key=lambda x: (x[1] - x[0]))
cnt = 0
for i, x in enumerate(val):
    if x[1] - x[0] <= 0:
        cnt +=1
if cnt >= k:
    print(0)
else:
    print(val[k-1][1]-val[k-1][0])