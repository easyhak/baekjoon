# 시험 감독  / 13458.py
# 알고리즘 분류: 수학, 사칙연산

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for x in A:
    
    if x > B:
        y = x - B
        ans += 1
        ans += y // C
        if y % C:
            ans += 1
    else:
        ans += 1
    
print(ans)