# 용감한 용사 진수 / 14718.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  C번
# 알고리즘 분류: 브루트포스 알고리즘, 값 / 좌표 압축
# pypy3로 제출, 시간복잡도가 너무 크다
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
soldier = []
for i in range(n):
    soldier.append(list(map(int,input().split())))
ans = 10000000
for i in range(n):
    for j in range(n):
        for w in range(n):
            a = soldier[i][0]
            b = soldier[j][1]
            c = soldier[w][2]
            count = 0
            for m in range(n):
                if (soldier[m][0]<=a) and (soldier[m][1]<=b) and (soldier[m][2]<=c):
                    count += 1
            if count >= k:
                ans = min(ans,(a+b+c))
print(ans)
    

