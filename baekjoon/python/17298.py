# 오큰수 / 17298.py
# 출처: 
# 알고리즘 분류: 자료구조, 스택

from collections import deque; import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
ans=[-1]*n
stack=deque()
# 스택을 이용해서 시간 복잡도가 O(n)으로 만들어줘야한다.
for i in range(n):
    while stack and (stack[-1][0] < arr[i]): 
        # 만약 값이 작다면 pop하고서 ans의 값을 바꿔주도록 한다.
        tmp, idx = stack.pop() 
        ans[idx]=arr[i]
    stack.append([arr[i],i]) # arr[i]값과 좌표를 넣어준다.
print(*ans)