import math
N = int(input())
room = list(map(int, input().split()))
a, b = map(int, input().split())

for x in room:
    if a > b:
        