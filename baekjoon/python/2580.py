# 스도쿠 / 2580.py
# 출처: Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 중등부 3번
# 알고리즘 분류: 백트래킹
import sys; input=sys.stdin.readline
sdoku=[]
for _ in range(9):
    sdoku.append(list(map(int,input().split())))
empty=[]
for i, arr in enumerate(sdoku):
    for j, x in enumerate(arr):
        if x==0:
            empty.append([i,j])

# 가능한 리스트
def possible_number(i, j):
    possbile_list = [1,2,3,4,5,6,7,8,9]  

    for k in range(9):
        if sdoku[i][k] in possbile_list:
            possbile_list.remove(sdoku[i][k])
        if sdoku[k][j] in possbile_list:
            possbile_list.remove(sdoku[k][j])
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sdoku[p][q] in possbile_list:
                possbile_list.remove(sdoku[p][q])
    
    return possbile_list
def back(depth, x,y):
    plist=list(possible_number(x,y)) 
    for k in plist:
        sdoku[x][y]=k
        if depth>=len(empty)-1:
            for ans in sdoku:
                print(*ans)
            exit(0)
        back(depth+1,*empty[depth+1])
        sdoku[x][y]=0 # 초기화
back(0,*empty[0])
