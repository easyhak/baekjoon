# 히스토그램에서 가장 큰 직사각형 / 6549.py
# 알고리즘 분류: 자료 구조, 세그먼트 트리, 분할 정복, 스택

from collections import deque
import sys

while True:
    rec = list(map(int,input().split()))
    n = rec.pop(0)
    if n == 0:
        break
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


## https://hooongs.tistory.com/330 정말 설명 잘해놓으신 듯