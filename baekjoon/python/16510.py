import sys

def binary_search(target):
    start = 0
    end = len(hap) - 1

    while start <= end:
        mid = (start + end) // 2
        if hap[mid] == target:
            return mid 
        elif hap[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return start-1
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
hap = []
s = 0
for i in arr:
    s+=i
    hap.append(s)

for _ in range(m):
    t = int(input())
    print(binary_search(t)+1)