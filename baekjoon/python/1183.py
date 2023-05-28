# 약속 / 1184.py
# 출처: 
# 알고리즘 분류: 수학, 정렬

n = int(input())
time_sub = []
for i in range(n):
    x,y = map(int,input().split())
    time_sub.append(x-y)
time_sub.sort()
if n%2 == 1:
    print(1)
else:
    print(time_sub[n//2]-time_sub[n//2-1]+1)