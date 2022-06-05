# 네 번째 점, 3009.py
# 출처: Contest > Croatian Open Competition in Informatics > COCI 2007/2008 > Contest #1 1번
# 알고리즘 분류: 구현, 기하학

x_list = []
y_list = []
# 3개의 숫자
for i in range(3):
    a, b = map(int,input().split())
    x_list.append(a)
    y_list.append(b)
cnt = x_list.count(x_list[0])
for i in range(len(x_list)):
    if x_list.count(x_list[i]) == 1:
        print(x_list[i], end=" ")
for i in range(len(y_list)):
    if y_list.count(y_list[i]) == 1:
        print(y_list[i])