from collections import deque

# 방향
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# 조각들을 담는 dictionary
pieces = {}


# table에서 조각을 찾는 메소드
def search_pieces(table, table_length):
    # 방문 유무 확인
    visited = [[False] * table_length for _ in range(table_length)]
    # table 칸 전체를 돌아다니며
    for i in range(table_length):
        for j in range(table_length):
            # 방문하지 않았으며 조각이 존재할 시
            if not visited[i][j] and table[i][j] == 1:
                # 조각 블럭 좌표가 담기는 리스트
                blocks = []
                q = deque()
                visited[i][j] = True
                q.append([j, i])
                blocks.append([j, i])
                # 최소 x와 최소 y, 최대 x와 최대 y 초기화
                xmin, ymin = j, i
                xmax, ymax = j, i

                # i,j 좌표 기준으로 너비우선탐색 시작
                while q:
                    x, y = q.popleft()
                    for dx, dy in dir:
                        px, py = x + dx, y + dy
                        # 범위 벗어날 시 다음 방향 수행
                        if not (0 <= px < table_length and 0 <= py < table_length):
                            continue
                        # 방문하지 않았으며 조각이 존재할 때
                        if not visited[py][px] and table[py][px] == 1:
                            # x의 최소,최대 및 y의 최대 최신화
                            # y의 최소값은 어차피 인덱스가 작은 곳부터 큰 곳으로 오기에
                            # 초기값이 최소값이 됨
                            if px < xmin:
                                xmin = px
                            elif px > xmax:
                                xmax = px
                            if py > ymax: ymax = py
                            # 방문 처리 및 블럭 좌표 추가 및 큐에 다음 수행 삽입
                            visited[py][px] = True
                            blocks.append([px, py])
                            q.append([px, py])
                # 전체 블럭 좌표에 대해
                # 정규화를 위해 x의 최소값과 y의 최소값을 빼줌
                for k in range(len(blocks)):
                    blocks[k][0] -= xmin
                    blocks[k][1] -= ymin
                # 원활한 비교를 위해 정렬
                blocks.sort(key=lambda x: (x[0], x[1]))
                # x의 최대/최소 차이와 y의 최대/최소 차이를 비교하여
                # 해당 조각의 boundary 지정
                bound = max((xmax - xmin + 1), (ymax - ymin + 1))

                # 해당 bound가 pieces 사전형에 없다면
                # blocks를 리스트 형태로 묶어서 넣어줌
                if bound not in pieces:
                    pieces[bound] = [blocks]
                # 아니라면 key값에 해당하는 리스트에 추가
                else:
                    pieces[bound].append(blocks)


def solution(game_board, table):
    answer = 0
    # table 길이
    table_length = len(table)
    # 조각 탐색 수행
    search_pieces(table, table_length)

    # game_board 길이
    board_length = len(game_board)
    # 방문 처리 리스트
    visited = [[False] * board_length for _ in range(board_length)]
    # 전체 game_board를 돌아다니며
    for i in range(board_length):
        for j in range(board_length):
            # 방문하지 않았으며 비어있는 칸일 시
            if not visited[i][j] and game_board[i][j] == 0:
                # 조각 블럭 좌표가 담기는 리스트
                blocks = []
                q = deque()
                visited[i][j] = True
                q.append([j, i])
                blocks.append([j, i])
                # 최소 x와 최소 y, 최대 x와 최대 y 초기화
                xmin, ymin = j, i
                xmax, ymax = j, i

                # i,j 좌표 기준으로 너비우선탐색 시작
                while q:
                    x, y = q.popleft()
                    for dx, dy in dir:
                        px, py = x + dx, y + dy
                        # 범위 벗어날 시 다음 방향 수행
                        if not (0 <= px < board_length and 0 <= py < board_length):
                            continue
                        # 방문하지 않았으며 빈 칸일 때
                        if not visited[py][px] and game_board[py][px] == 0:
                            # x의 최소,최대 및 y의 최대 최신화
                            # y의 최소값은 어차피 인덱스가 작은 곳부터 큰 곳으로 오기에
                            # 초기값이 최소값이 됨
                            if px < xmin:
                                xmin = px
                            elif px > xmax:
                                xmax = px
                            if py > ymax: ymax = py
                            # 방문 처리 및 블럭 좌표 추가 및 큐에 다음 수행 삽입
                            visited[py][px] = True
                            blocks.append([px, py])
                            q.append([px, py])
                # 빈칸 좌표들에 대해
                # 정규화를 위해 x의 최소값과 y의 최소값을 빼줌
                for k in range(len(blocks)):
                    blocks[k][0] -= xmin
                    blocks[k][1] -= ymin
                # 원활한 비교를 위해 정렬
                blocks.sort(key=lambda x: (x[0], x[1]))
                # x의 최대/최소 차이와 y의 최대/최소 차이를 비교하여
                # 해당 빈칸의 boundary 지정
                bound = max((xmax - xmin + 1), (ymax - ymin + 1))
                # 해당 boundary가 pieces에 있다면
                if bound in pieces:
                    # boundary에 포함된 조각들을 하나씩 넣어봄
                    for p, piece in enumerate(pieces[bound]):
                        # 조각 찾았는지 여부에 대한 flag
                        flag = False
                        # 정방향, 90도 회전, 180도 회전, 270도 회전 수행
                        for _ in range(4):
                            # 해당 조각이 block과 같으면
                            if piece == blocks:
                                # 중복되어 쓰이지 않도록 하기 위해 제거
                                pieces[bound].pop(p)
                                # 블럭의 좌표 수를 결과값에 더해줌
                                answer += len(blocks)
                                flag = True
                                break
                            # 같지 않다면
                            else:
                                # 새로운 리스트 생성해서
                                new_piece = []
                                # 90도 회전시킨 좌표값을 돌려줌
                                for x, y in piece:
                                    new_piece.append([bound - y - 1, x])

                                # 회전 후 정규화가 제대로 되어있지 않은 경우를 우해
                                # 다시 한번 정규화
                                row_min = new_piece[0][0]
                                for rw, _ in new_piece:
                                    if row_min > rw: row_min = rw
                                if row_min > 0:
                                    for r in range(len(new_piece)):
                                        new_piece[r][0] -= row_min
                                # 원활한 비교를 위해 좌표 정렬
                                new_piece.sort(key=lambda x: (x[0], x[1]))

                                # 다음 탐색해야 할 조각을 90도 회전한 조각으로 지정
                                piece = [a[:] for a in new_piece]

                        # 찾았을 시 해당 빈 칸에서 탐색 종료
                        if flag: break

    return answer