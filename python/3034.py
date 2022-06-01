import sys
input = sys.stdin.readline

n,w,h = map(int,input().split())
for i in range(n):
    match = int(input())
    if w**2+h**2 >= match **2:
        print("DA")
    else:
        print("NE")
