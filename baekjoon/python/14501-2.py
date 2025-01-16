# 퇴사
# 백트래킹 풀이

n = int(input())
t = []
p = []
ans = 0

def backtrack(depth, s):
    global t
    global p
    global ans
    # 끝나는 조건
    if depth >= n:
        ans = max(ans, s)
        return
    # 최대 수익
    # 선택했으면
    # 선택을 할 수 있는지도 확인해야함
    if depth + t[depth] <= n:
        backtrack(depth + t[depth], s + p[depth])

    # 선택 안했으면
    backtrack(depth + 1, s)


for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
backtrack(0, 0)

print(ans)