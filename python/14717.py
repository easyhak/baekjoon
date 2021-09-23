# 14717.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  B번
# 알고리즘: 구현

import sys
input = sys.stdin. readline

a,b = map(int, input().split())
arr = []
for i in range(1,11):
    if i == a:
        continue
    for j in range(1,11):
        if j == b:
            continue
        arr.append((i,j))
count = 0
if a == b:
    for x, y in arr:
        if x == y and x > a:
            count += 1
    print("%.3f"%(1-count/153))
elif a != b:
    for x, y in arr:
        if (a+b)%10 > (x+y)%10 and x != y:
            count += 1
    count *= 2
    print("%.3f"%(count/153))

