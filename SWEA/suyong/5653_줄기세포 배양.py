for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())

    # 배열 최대크기 선언. 세포는 최대 2초에 1번 번식할 수 있음. 
    grid = [[0] * (M + K) for _ in range(N+K)]
    visited = [[False] * (M + K) for _ in range(N + K)]
    input_cells = [list(map(int, input().split())) for _ in range(N)]
    
    cells = []
    for r in range(N):
        for c in range(M):
            life = input_cells[r][c]
            if life > 0:
                #생명력, 수명
                grid[K // 2 + r][K // 2 + c] = [life, life]
                cells.append([K // 2+r, K // 2+c])

    for time in range(K):
        # 번식된 세포 리스트
        new_cells = []
        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0], cells[i][1]
            # 세포 비활성 상태.
            if grid[r][c][1] > 0:
                grid[r][c][1] -= 1
            # 세포 활성상태. 분열 시도. 이미 분열했던 세포는 컷.
            elif grid[r][c][1] == 0 and not visited[r][c]:
                visited[r][c] = True
                life = grid[r][c][0]
                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    if grid[r+dr][c+dc] == 0:
                        new_cells.append([r+dr, c+dc, life])
                # 생명력 감소
                grid[r][c][0] -= 1
            # 생명력 깎이는 중
            else:
                if grid[r][c][0] > 0:
                    grid[r][c][0] -= 1
                #죽은 세포 제거. 격자에는 남아있음.
                else: cells.pop(i)
        # 번식된 세포 추가
        for new_cell in new_cells:
            r, c, life = new_cell
            if grid[r][c] == 0:
                grid[r][c] = [life, life]
                cells.append([r, c])
            else:
                # 생명력이 더 센 세포가 우선.
                if grid[r][c][0] < life:
                    grid[r][c] = [life, life]
    answer = 0
    # 활성 + 비활성 세포 개수
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] and grid[r][c][0] > 0:
                answer += 1

    print("#{} {}".format(tc, answer))