def dfs(y, x, c):
    global cnt, answer

    # y 좌표 범위 벗어나면 값 비교 후 리턴
    if y >= 10:
        answer = min(answer, c)
        return
    # x 좌표 범위 벗어나면 다음 행 0열부터 확인
    if x >= 10:
        dfs(y + 1, 0, c)
        return

    # 1이 적힌 칸이라면 해당 위치에 1~5 사이즈의 색종이 놓을 수 있는 지 확인
    if paper[y][x] == 1:
        for size in range(5):
            # 확인하려는 사이즈의 색종이가 이미 5장 사용했으면 다음 사이즈 비교
            if cnt[size] == 5:
                continue
            # 현재 위치에서 색종이를 놓았을 때 가장 끝 자리가 범위를 벗어나면 다음 사이즈 비교
            if y + size >= 10 or x + size >= 10:
                continue

            # (y, x)에 size 크기의 색종이를 놨을 때 그 자리에 0이 있는지 확인
            flag = True
            for i in range(y, y + size + 1):
                for j in range(x, x + size + 1):
                    if paper[i][j] == 0:
                        flag = False
                        break
                if not flag:
                    break

            # 0이 없다면 -> 색종이 놓기
            if flag:
                for i in range(y, y + size + 1):
                    for j in range(x, x + size + 1):
                        # 0이 적힌 칸은 색종이 있으면 안되니까 값 0으로 바꾸기
                        paper[i][j] = 0
                # 해당 사이즈에 갯수 1증가
                cnt[size] += 1
                # 다음 칸 확인
                dfs(y, x + size + 1, c + 1)
                # 방문처리? 한거 해제하기
                for i in range(y, y + size + 1):
                    for j in range(x, x + size + 1):
                        paper[i][j] = 1
                cnt[size] -= 1
    else:
        dfs(y, x + 1, c)

# 입력
paper = [list(map(int, input().split())) for _ in range(10)]
# 크기별로 몇개 썼는지 저장할 리스트
cnt = [0] * 5
# 출력할 값
answer = 1e9

dfs(0, 0, 0)

# 모두 덮는 것이 불가능하면 -1, 아니면 색종이의 최소 개수 출력
if answer != 1e9:
    print(answer)
else:
    print(-1)