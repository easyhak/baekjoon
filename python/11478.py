# 서로 다른 부분 문자열의 개수 / 11478.py
# 출처: 
# 알고리즘 분류: 자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

x = str(input())
s = set(x)
for i in range(len(x)+1):
    for j in range(i+1,len(x)+1):
        s.add(str(x[i:j]))
print(len(s))