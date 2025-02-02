from collections import deque
n, w, l = map(int, input().split())

trucks = deque(list(map(int, input().split())))

ans = 0

bridge = deque([0]*w)
bridge_sum = 0

bridge[0] = trucks.popleft()
ans += 1
bridge_sum += bridge[0]

def shift_array(arr: deque):
    global bridge_sum
    bridge_sum -= arr.pop()
    arr.appendleft(0)

while trucks:
    # 들어갈 수 있으면 넣어주기
    # 길이 비교, 무게 비교
    shift_array(bridge)

    if trucks[0] + bridge_sum <= l:
        t = trucks.popleft()
        bridge[0] = t
        bridge_sum += t
    ans += 1
for i, x in enumerate(bridge):
    if x != 0:
        ans += w - i
        break
print(ans)
