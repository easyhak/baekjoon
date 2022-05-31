# 대칭 차집합 / 1269.py
# 출처: 
# 알고리즘 분류: 자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

x = input()
A = set(input().split())
B = set(input().split())
print(len(A-B)+len(B-A))