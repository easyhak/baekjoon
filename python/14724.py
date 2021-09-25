# 관리자는 누구? / 14724.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  I번
# 알고리즘 분류: 구현
m = 0
n = int(input())
cnt = 0
for i in range(9):
    arr = list(map(int, input().split()))
    s = max(arr)
    if m < s:
        m = s
        cnt = i
if cnt == 0:
    print("PROBRAIN")
elif cnt == 1:
    print("GROW")
elif cnt == 2:
    print("ARGOS")
elif cnt == 3:
    print("ADMIN")
elif cnt == 4:
    print("ANT")
elif cnt == 5:
    print("MOTION")
elif cnt == 6:
    print("SPG")
elif cnt == 7:
    print("COMON")
elif cnt == 8:
    print("ALMIGHTY")