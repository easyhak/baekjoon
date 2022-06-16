# 가장 긴 바이토닉 부분 수열 / 11054.py
# 알고리즘 분류: 다이나믹 프로그래밍
n=int(input())
arr=list(map(int,input().split()))
dpHigh=[1]*n
dpLow=[1]*n
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dpHigh[i]=max(dpHigh[i],dpHigh[j]+1)
        if arr[n-1-i]>arr[n-1-j]:
            dpLow[n-1-i]=max(dpLow[n-1-i],dpLow[n-1-j]+1)
ans=1
for i in range(n):
    ans=max(ans,dpHigh[i]+dpLow[i]-1)
print(ans)
