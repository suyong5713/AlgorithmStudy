t = int(input())
for test in range(1,t+1):
    n = int(input())
    # 예외처리가 번거로워 테두리에 칸 하나 더 생성함
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    arr.insert(0,[0]*(n+2))
    arr.append([0]*(n+2))
    visited = [[False]*(n+2) for _ in range(n+2)]
    res_list = []

    for i in range(1,n+1):
        for j in range(1,n+1):
            # 방문하지 않았고 0이 아니라면
            # 행렬의 (0,0) 원소를 만남
            if not visited[i][j] and arr[i][j] != 0:
                x,y = j,i
                # 행렬의 마지막 원소(n*n 행렬일 시 (n-1,n-1)원소) 탐색
                while arr[y][x+1] != 0:
                    x += 1
                while arr[y+1][x] != 0:
                    y += 1

                # 행렬의 행과 열의 크기를 구함
                dx,dy = x-j+1,y-i+1
                res_list.append((dy,dx,dy*dx))
                # 탐색 완료한 행렬에 대해서 방문 처리
                for py in range(i,y+1):
                    for px in range(j,x+1):
                        visited[py][px] = True
    # 우선순위를 1순위로 크기, 2순위로 행 길이로 하여 정렬
    res_list.sort(key = lambda x: (x[2],x[0]))

    s = ''
    s += (str(len(res_list))+' ')
    for res in res_list:
        s += (str(res[0]) + ' ')
        s += (str(res[1]) + ' ')

    print("#{} {}".format(test, s))