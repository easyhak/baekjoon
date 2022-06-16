# 가장 긴 증가하는 부분 수열 2 / 12015.py
# 알고리즘 분류: 이분 탐색, 가장 긴 증가하는 부분 수열: o(n log n)


def binary_search(arr, target):
    low=0
    high=len(arr)-1
    while(low < high):
        mid=(high+low)//2
        if target > arr[mid]:
            low=mid+1
        else: high=mid
    return high
n=int(input())
arr=list(map(int,input().split()))
record=[]
for i in arr:
    # record가 비어어있으면 append
    if not record:
        record.append(i)
    # i와 record[-1]을 비교
    elif record[-1]<i:
        record.append(i)
    else:
        ind=binary_search(record, i)
        record[ind]=i
# 길이만 얻을 수 있음, 실제 증가하는 수열과는 다름
print(len(record))
