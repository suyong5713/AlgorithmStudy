# 전체 cctv가 가질 수 있는 경우의 수에 대해 리스트로 나타냄
cctv=[[],
      [[(1,0)],[(-1,0)],[(0,1)],[(0,-1)]],  # cctv1
      [[(1,0),(-1,0)],[(0,1),(0,-1)]],      # cctv2
      [[(-1,0),(0,1)],[(0,-1),(1,0)],[(-1,0),(0,-1)],[(1,0),(0,1)]],    # cctv3
      [[(-1,0),(0,1),(0,-1)],[(1,0),(0,1),(0,-1)],[(1,0),(-1,0),(0,-1)],[(1,0),(-1,0),(0,1)]],  # cctv4
      [[(1,0),(-1,0),(0,1),(0,-1)]]]    # cctv5


def DFS(idx, arr, blank):   # 매개변수: 탐색할 cctv idx, cctv 맵, 남은 사각지대
    global res, idx_max
    # 모든 cctv를 탐색했다면
    if idx == idx_max:
        # 최소 사각지대 개수 최신화 및 종료
        if res > blank:
            res = blank
        return

    # cctv종류, 위치 init
    type = location[idx][0]
    x,y = location[idx][1], location[idx][2]
    # 해당 cctv가 가질 수 있는 모든 경우의 수에 대해
    for case in cctv[type]:
        # deepcopy
        buff = [ar[:] for ar in arr]
        total = blank
        # 해당 방향들로 감시 영역 체크
        for dx,dy in case:
            cx,cy = x,y
            while True:
                cx,cy = cx+dx,cy+dy
                # 맵을 벗어나거나 벽을 만난다면 반복문 탈출
                # 아니라면 체크하면서 계속 진행
                if not(0 <= cx < w and 0 <= cy < h): break
                if buff[cy][cx] == 0:
                    buff[cy][cx] = '#'
                    total -= 1
                elif arr[cy][cx] == 6: break
        DFS(idx+1,buff,total)


# init
h,w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
location = []
idx_max = 0     # cctv 개수
total = h*w     # 초기 사각지대 개수
for i in range(h):
    for j in range(w):
        if arr[i][j] != 0:
            total -= 1
            if arr[i][j] != 6:
                location.append((arr[i][j],j,i))
                idx_max += 1
res = float('inf')
# 2차원 배열 deepcopy 방법
buff = [ar[:] for ar in arr]
DFS(0,buff,total)
print(res)