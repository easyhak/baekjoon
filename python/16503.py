# 괄호 없는 사칙연산 / 16503.py
# 출처: University > 충남대학교 > 제2회 생각하는 프로그래밍 대회 A번
# 알고리즘 분류: 다이나믹 프로그래밍

s = list(input().split())
arr = [s[0],s[2],s[4]]
number = list(map(int,arr))
op = [s[1], s[3]]
a= number[0]
b= number[2]
for i in range(2):
    if op[i] == "*":
        a *= number[i+1]
    elif op[i] == "/":
        if a < 0:
            a = -a
            a //= number[i+1]
            a = -a
        else:
            a //= number[i+1]
    elif op[i] == "-":
        a -= number[i+1]
    elif op[i] == "+":
        a += number[i+1]
for i in range(1,-1,-1):
    if op[i] == "*":
        b *= number[i]
    elif op[i] == "/":
        if b < 0:
            b = -b
            b = number[i] // b
            b = - b
        else:
            b = number[i] // b
    elif op[i] == "-":
        b = number[i] - b
    elif op[i] == "+":
        b += number[i]
if a < b:
    print(a)
    print(b)
else:
    print(b)
    print(a)
