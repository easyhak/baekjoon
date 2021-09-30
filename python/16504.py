# 종이접기 / 16504.py
# 출처: University > 충남대학교 > 제2회 생각하는 프로그래밍 대회 B번
# 알고리즘 분류: 수학, 구현, 사칙연산

n=int(input())
s=0
for i in range(n):
    arr=list(map(int,input().split()))
    s+=sum(arr)
print(s)