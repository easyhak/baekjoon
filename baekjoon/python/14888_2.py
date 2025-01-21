# 연산자 끼워넣기, 14888.py
# 알고리즘 분류: 백트래킹, 브루트포스 알고리즘

N = map(int, input().split())
arr = list(map(int, input().split()))
# 덧셈 뺄셈 곱셈 나눗셈

a, b, c, d = list(map(int, input().split()))
min_ans = 10_000_000_000
max_ans = -10_000_000_000

def calc(arr, op_list):
    
    val = arr[0]
    for i, x in enumerate(op_list):
        if x == "+":
            val = val + arr[i+1]
        elif x == "-":
            val = val - arr[i+1]
        elif x == "*":
            val = val * arr[i+1]
        elif x == "/":
            if val < 0:
                val = -val
                val  = val // arr[i+1]
                val = -val
            else:
                val = val // arr[i+1]
    return val

def backtrack(plus, minus, multiple, divider, st):
    # 종료 조건
    global min_ans
    global max_ans
    if a == plus and b == minus and c == multiple and divider == d:
        v = calc(arr, st)
        max_ans = max(max_ans, v)
        min_ans = min(min_ans, v)
    # 추가할 수 있는 경우에만 추가하기

    if a > plus:
        backtrack(plus + 1, minus, multiple, divider, st + ["+"])
    if b > minus:
        backtrack(plus, minus + 1, multiple, divider, st + ["-"])
    if c > multiple:
        backtrack(plus, minus, multiple + 1, divider, st + ["*"])
    if d > divider:
        backtrack(plus, minus, multiple, divider + 1, st + ["/"])
backtrack(0, 0, 0, 0, [])



print(max_ans)
print(min_ans)