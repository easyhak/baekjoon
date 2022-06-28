# 가장 긴 증가하는 부분 수열 4,5 / 14002.py / 14003.py
# 알고리즘 분류: 다이나믹 프로그래밍
def binary_search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(high+low)//2
        if target==arr[mid]:
            return mid
        elif target>=arr[mid]:
            low=mid+1
        else: high=mid-1
    return low

n=int(input())
arr=list(map(int,input().split()))
LIS=[]
record=[]
for i in arr:
    if not LIS:
        LIS.append(i)
        record.append(1)
    elif LIS[-1]<i:
        LIS.append(i)
        record.append(len(LIS))
    else:
        ind=binary_search(LIS,i)
        LIS[ind]=i
        record.append(ind+1)
M=len(LIS)
print(M)
ans=[]
for i in range(n-1,-1,-1):
    tmp=1000
    if record[i]==M:
        M-=1
        ans.append(arr[i])
    if M==0:
        break
print(*ans[::-1])