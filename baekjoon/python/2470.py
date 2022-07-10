# 두 용액 / 2470.py
# 알고리즘 분류: 정렬, 이분 탐색, 두 포인터
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
left,right = 0, n-1
min_value = 2000000000
ans1, ans2 = 0,0
while(left < right):
    s = arr[left]+arr[right]
    if abs(s) < min_value:
        min_value = abs(s)
        ans1, ans2 = arr[left], arr[right]
    if min_value == 0:
        break
    if s < 0:
        left = left + 1
    elif s > 0:
        right = right - 1
print(ans1, ans2)