places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
direction = [[-1,0],[1,0],[0,-1],[0,1]]
dfs_result = []
def DFS(depth, room, row, col, visited, log):
    global dfs_result
    #맨해튼 거리 1위치 즉, 바로 옆에 응시자가 앉으면 거리두기 준수 X
    if depth == 1:
        if room[row][col] == "P":
            dfs_result.append(False)
            return
    #맨해튼 거리 2 위치에 응시자가 있는 경우 
    #탐색 경로에 파티션이 없으면 거리두기 준수 X
    elif depth == 2:
        if room[row][col] == "P" and "X" not in log:
            dfs_result.append(False)
        return 
    #4방 탐색
    for i in range(4):
        dr, dc = direction[i]
        nr, nc = row + dr, col + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                #탐색 경로 log에 저장
                log.append(room[nr][nc])
                DFS(depth+1, room, nr, nc, visited, log)
                visited[nr][nc] = False
                log.pop()

def solution(places):
    #DFS 결과를 담을 배열
    global dfs_result
    #5개 방의 거리두기 준수 여부.
    answer = [1,1,1,1,1]
    for idx,room in enumerate(places):
        dfs_result = []
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    #응시자 위치에서 DFS 탐색
                    visited = [[False] * 5 for _ in range(5)]
                    visited[i][j] = True
                    DFS(0, room, i, j, visited, [])
                    #한명이라도 거리두기 준수하지 않으면 0
                    if False in dfs_result:
                        answer[idx] = 0
                        break
            if False in dfs_result:
                break
    print(answer)
    return answer
solution(places)