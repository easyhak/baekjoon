# 우유 축제 / 14720.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  E번
# 알고리즘 분류: 구현

n = int(input())
arr = list(map(int,input().split()))
count = 0
for x in arr:
    if x == count % 3:
        count += 1
    else:
        continue
print(count)