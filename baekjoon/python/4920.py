

# 1-1. ----
def one_one(board, N):
    global ans
    for i in range(N):
        for j in range(N-3):
            ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3])
# 1-2. |
def one_two(board, N):
    global ans
    for i in range(N-3):
        for j in range(N):
            ans = max(ans, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])

# 2-1.
def two_one(board, N):
    global ans
    for i in range(N-1):
        for j in range(N-2):
            ans = max(ans, board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2])

# 2-2
def two_two(board, N):
    global ans
    for i in range(N-2):
        for j in range(N-1):
            ans = max(ans, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])

# 3-1
def three_one(board, N):
    global ans
    for i in range(N-1):
        for j in range(N-2):
            ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2])
# 3-2
def three_two(board, N):
    global ans
    for i in range(N-2):
        for j in range(N-1):
            ans = max(ans, board[i][j+1] + board[i+1][j+1] + board[i+2][j] + board[i+2][j+1])

# 3-3
def three_three(board, N):
    global ans
    for i in range(N-1):
        for j in range(N-2):
            ans = max(ans, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2])

# 3-4
def three_four(board, N):
    global ans
    for i in range(N-2):
        for j in range(N-1):
            ans = max(ans, board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j])

# 4-1
def four_one(board, N):
    global ans
    for i in range(N-1):
        for j in range(N-2):
            ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1])

# 4-2
def four_two(board, N):
    global ans
    for i in range(N-2):
        for j in range(N-1):
            ans = max(ans, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1])

# 4-3
def four_three(board, N):
    global ans
    for i in range(N-1):
        for j in range(N-2):
            ans = max(ans, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2])

# 4-4
def four_four(board, N):
    global ans
    for i in range(N-2):
        for j in range(N-1):
            ans = max(ans, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])

# 5-1
def five_one(board, N):
    global ans
    for i in range(N-1):
        for j in range(N-1):
            ans = max(ans, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i][j+1])

test_case_cnt = 1

while True:
    N = int(input())
    if N == 0:
        break
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    ans = -1_000_000_000

    one_one(board, N)
    one_two(board, N)
    two_one(board, N)
    two_two(board, N)
    three_one(board, N)
    three_two(board, N)
    three_three(board, N)
    three_four(board, N)
    four_one(board, N)
    four_two(board, N)
    four_three(board, N)
    four_four(board, N)
    five_one(board, N)
    print(f"{test_case_cnt}. {ans}")
    test_case_cnt+=1
    