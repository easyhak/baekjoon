# 부분합 / 1806.py
# 알고리즘 분류: 투 포인터
n, s = map(int, input().split())
arr = list(map(int,input().split()))
prefix_sum = [0]

for i in arr:
    prefix_sum.append(i+prefix_sum[-1])
ans = 100001
left, right = 0, 1
while left<right and right < n+1:
    if prefix_sum[right]-prefix_sum[left] < s:
        right += 1
    else: 
        if ans > right - left:         
            ans= right - left
        left+=1

print (0 if ans == 100001 else ans)