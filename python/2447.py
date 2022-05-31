# 별 찍기 - 10 / 2447.py
# 출처: 
# 알고리즘 분류: 분할 정복, 재귀
n = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']
    arr = star(l//3)
    stars = []
    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars

print('\n'.join(star(n)))