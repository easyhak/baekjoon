# 좋은 단어, 3986.py
# 출처: Contest > Croatian Open Competition in Informatics > COCI 2012/2013 > Contest #4 2번
# 알고리즘 분류: 자료구조, 스택
n = int(input())
ans = 0
for i in range(n):
    s = list(input().rstrip())
    stack = [False]
    for x in s:
        if stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    if len(stack) == 1:
        ans+=1
print(ans)