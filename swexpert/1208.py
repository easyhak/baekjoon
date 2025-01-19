for i in range(10):
    n = int(input())
    
    boxes = list(map(int, input().split()))
    for x in range(n):
    # 최솟값에서 최댓값 넣어주기
        M = max(boxes)
        m = min(boxes)
        boxes[boxes.index(M)] = boxes[boxes.index(M)] - 1
        boxes[boxes.index(m)] = boxes[boxes.index(m)] + 1
    print(f"#{i+1} {max(boxes) - min(boxes)}")
    