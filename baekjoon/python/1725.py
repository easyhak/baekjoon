# 히스토그램 / 1725.py
# 알고리즘 분류: 자료 구조, 세그먼트 트리, 분할 정복, 스택

from collections import deque
import sys; input = sys.stdin.readline


n = int(input())
rec = []
for i in range(n):
    rec.append(int(input()))
stack = deque()
ans = 0
for i in range(n):
    while len(stack)!=0 and rec[stack[-1]] > rec[i]:
        tmp=stack.pop()
        if len(stack) == 0:
            width = i
        else:
            width = i - stack[-1]-1
        ans = max(ans, width * rec[tmp])
    stack.append(i)

while len(stack) !=0:
    tmp = stack.pop()

    if len(stack) == 0:
        width = n
    else:
        width = n - stack[-1] - 1
    ans = max(ans, width * rec[tmp])
print(ans)
