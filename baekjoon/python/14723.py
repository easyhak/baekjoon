# 이산수학 과제 / 14723.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  E번
# 알고리즘 분류: 수학, 구현

n = int(input())
i = 1
while (n > i):
    n -= i
    i+=1
print(i+1-n, n)