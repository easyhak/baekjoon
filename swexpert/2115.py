t = int(input())
for test_case in range(t):
    board = []
    n, m, c = map(int, input().split())
    for i in range(n):
        board.append(list(map(int, input().split())))
    ans = 0

    def max_honey(honey_list, c):
        max_profit = 0
        length = len(honey_list)
        for mask in range(1, 1 << length):
            total = 0
            profit = 0
            for i in range(length):
                if mask & (1 << i):
                    total += honey_list[i]
                    profit += honey_list[i] ** 2
            if total <= c and profit > max_profit:
                max_profit = profit
        return max_profit
    for i in range(n):
        for j in range(n-m+1):
            first_list:list = board[i][j:j+m]
            first_profit  = max_honey(first_list, c)
                # 만약 p의 
            # 한 개를 먼저 선택하고 그 중에 되는지 확인하기
            # j 값만큼 더하기
            for x in range(n):
                for y in range(n-m+1):
                    # 위에서 이미 선택한 값인지 확인하기
                    if x == i and (j<=y<=j+m or y<=j<=y+m):
                        continue
                    
                    second_list = board[x][y:y+m]
                    
                    second_list.sort(reverse=True)
                    second_profit  = max_honey(second_list, c)
                    
                    #####
                    # print("==============")
                    # print(first_list)
                    # print(second_list)
                    # if first_list == second_list:
                    #     print(i,j)
                    #     print(x,y)
                    # print(first_profit)
                    # print(second_profit)
                    # print(first_profit + second_profit)
                    ans = max(ans, first_profit + second_profit)
    print(f"#{test_case+1} {ans}")