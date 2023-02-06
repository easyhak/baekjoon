# 중복 빼고 정렬하기 / 10867.py
# 알고리즘 분류: 정렬

n = int(input())
numbers = sorted(list(set(map(int,input().split()))))
print(*numbers)