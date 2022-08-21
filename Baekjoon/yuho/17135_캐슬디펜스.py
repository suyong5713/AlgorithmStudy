from itertools import combinations

h,w,d = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(h)]

# 사정거리가 1이라면
# 열에 몬스터가 많은 곳일수록 많이 잡을 수 있음
# 몬스터가 많은 열을 탐색하여 해당 상위 3열의 몬스터 수를 합하여 출력
if d == 1:
    t_arr = list(list(zip(*tmp)))
    m = [sum(a) for a in t_arr]
    m.sort(reverse=True)
    print(sum(m[:3]))
# 사정거리가 1보다 크다면
else:
    mm = 0
    res = 0
    # 몬스터 수 카운트
    for i in range(h):
        for j in range(w):
            if tmp[i][j] == 1: mm += 1

    # 궁수를 배치하는 모든 경우의 수에 대해
    for a1,a2,a3 in combinations(range(w),3):
        # deepcopy
        arr = [t[:] for t in tmp]
        # 3명의 궁수 위치 초기화
        archer = [(h,a1),(h,a2),(h,a3)]
        hit = 0
        monster = mm
        # 몬스터가 모두 없어질 때까지 반복
        while monster > 0:
            shoot = [False]*3
            visited = [[False] * w for _ in range(h)]
            # 궁수 하나하나에 대해
            for j, (y, x) in enumerate(archer):
                success = False
                # 아직 몬스터를 쏘지 않은 궁수일 시
                if not shoot[j]:
                    # 사정거리 1 ~ d만큼 탐색 : 가까운 몬스터 먼저 사냥해야 하므로
                    for dd in range(1,d+1):
                        # 사정거리 공식
                        for i in range(-dd+1,dd):
                            px = x+i
                            if i <= 0: i *= -1
                            py = y-dd+i
                            # 해당 사정거리 위치가 맵 밖을 나가지 않고
                            if 0 <= px < w and 0 <= py < h:
                                # 그 위치에 몬스터가 있다면
                                if arr[py][px] == 1:
                                    # 몬스터가 아처에게 겨냥되었음을 표시, 해당 헌터가 쐈음을 표시
                                    visited[py][px] = True
                                    shoot[j] = True
                                    success = True
                                    break
                        if success: break
            # 방문된(화살에 맞은)몬스터에 대해
            # 맵을 0으로 만들고 맞은 몬스터 카운트 증가, 몬스터 수 감소
            for r in range(h):
                for c in range(w):
                    if visited[r][c]:
                        arr[r][c] = 0
                        hit += 1
                        monster -= 1

            # 시뮬레이션
            # 맵을 한 칸씩 내리면서 몬스터 수 감소
            for ar in arr[h-1]:
                if ar == 1: monster -= 1
            for i in range(h-2,-1,-1):
                for j in range(w):
                    arr[i+1][j] = arr[i][j]
            arr[0] = [0]*w
        # 최대값 최신화
        if res < hit: res = hit

    print(res)
