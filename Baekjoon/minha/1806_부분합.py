N, S = map(int, input().split())
num = list(map(int, input().split()))

answer = 1e9
start = 0
end = 0
acc_sum = 0

while True:
    # 수열의 합이 s를 넘으면
    if acc_sum >= S:
        # 값 갱신
        answer = min(answer, end - start)
        # 현재 수열의 시작값을 누적합에서 빼고, 시작 위치 한 칸 이동
        acc_sum -= num[start]
        start += 1

    # 수열의 합이 s를 넘지 않는다면
    else:
        # 맨 끝 위치 도착 시 반복을 멈춤
        if end == N:
            break
        # 현재 수열의 끝값을 누적합에 더해주고, 끝 위치 한 칸 이동
        acc_sum += num[end]
        end += 1

if answer == 1e9:
    print(0)
else:
    print(answer)