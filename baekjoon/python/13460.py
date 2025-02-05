from collections import deque

n, m = map(int, input().split())
board = []
red = (0, 0)
blue = (0, 0)
hole = (0, 0)

for i in range(n):
    row = list(input().strip())
    board.append(row)
    for j in range(m):
        if row[j] == 'R':
            red = (i, j)
        elif row[j] == 'B':
            blue = (i, j)
        elif row[j] == 'O':
            hole = (i, j)

def move_ball(x, y, dx, dy, board, other_ball):
    while True:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == '#':
            return (x, y)
        if (nx, ny) == other_ball and board[nx][ny] != 'O':
            return (x, y)
        if board[nx][ny] == 'O':
            return (nx, ny)
        x, y = nx, ny

def tilt(red_pos, blue_pos, direction):
    dx, dy = 0, 0
    if direction == 'U':
        dx = -1
    elif direction == 'D':
        dx = 1
    elif direction == 'L':
        dy = -1
    elif direction == 'R':
        dy = 1
    
    # 이동 순서 결정
    order_red_first = False
    if direction == 'U' and red_pos[0] < blue_pos[0]:
        order_red_first = True
    elif direction == 'D' and red_pos[0] > blue_pos[0]:
        order_red_first = True
    elif direction == 'L' and red_pos[1] < blue_pos[1]:
        order_red_first = True
    elif direction == 'R' and red_pos[1] > blue_pos[1]:
        order_red_first = True
    
    # 구슬 이동
    if order_red_first:
        new_red = move_ball(*red_pos, dx, dy, board, blue_pos)
        new_blue = move_ball(*blue_pos, dx, dy, board, new_red)
    else:
        new_blue = move_ball(*blue_pos, dx, dy, board, red_pos)
        new_red = move_ball(*red_pos, dx, dy, board, new_blue)
    
    # 위치 조정 (구슬이 겹치고 구멍이 아닌 경우)
    if new_red == new_blue and board[new_red[0]][new_red[1]] != 'O':
        if direction == 'U':
            if order_red_first:
                new_blue = (new_blue[0] + 1, new_blue[1])
            else:
                new_red = (new_red[0] + 1, new_red[1])
        elif direction == 'D':
            if order_red_first:
                new_blue = (new_blue[0] - 1, new_blue[1])
            else:
                new_red = (new_red[0] - 1, new_red[1])
        elif direction == 'L':
            if order_red_first:
                new_blue = (new_blue[0], new_blue[1] + 1)
            else:
                new_red = (new_red[0], new_red[1] + 1)
        elif direction == 'R':
            if order_red_first:
                new_blue = (new_blue[0], new_blue[1] - 1)
            else:
                new_red = (new_red[0], new_red[1] - 1)
    
    return new_red, new_blue

visited = {}
queue = deque([(red, blue, 0)])
visited[(red, blue)] = 0
answer = -1

while queue:
    current_red, current_blue, cnt = queue.popleft()
    
    if cnt > 10:
        continue
    if current_red == hole and current_blue != hole:
        answer = cnt
        break
    
    for direction in ['U', 'D', 'L', 'R']:
        new_red, new_blue = tilt(current_red, current_blue, direction)
        
        # 파란 구슬이 구멍에 들어간 경우 스킵
        if new_blue == hole:
            continue
        
        # 방문 체크: 더 적은 이동 횟수로 도달했을 때만 업데이트
        state = (new_red, new_blue)
        if state not in visited or cnt + 1 < visited[state]:
            visited[state] = cnt + 1
            if cnt + 1 <= 10:
                queue.append((new_red, new_blue, cnt + 1))

print(answer if answer != -1 and answer <= 10 else -1)