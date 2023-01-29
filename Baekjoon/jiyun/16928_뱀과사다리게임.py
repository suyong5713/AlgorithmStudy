from collections import deque
BOARD = 101
MOVES = [1, 2, 3, 4, 5, 6]

def solution(_start):                                  # [2] 솔루션 도출 : 최단 거리 (BFS)
    queue = deque([_start])                                      # 게임 시작 -> 1부터 시작
    visited[_start] = True
    while queue:
        now_x = queue.popleft()
        if now_x==BOARD-1: return arr[now_x]
        for move in MOVES:                                  # 주사위 굴림
            next_x = now_x + move
            if next_x<BOARD and not visited[next_x]:
                if next_x in ladder.keys():                # 사다리, 뱀 체크
                    next_x = ladder[next_x]
                if next_x in snake.keys():
                    next_x = snake[next_x]
                if not visited[next_x]:                     # 도착한 좌표가 방문한 적이 없는 경우
                    visited[next_x] = True
                    arr[next_x] = arr[now_x] + 1            # 최단 거리 기록
                    queue.append(next_x)
    return False

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    n, m = map(int, input().split())                    # [1] 데이터 입출력
    arr = [0]*101                                       # 보드 생성 -> 단, 1부터 시작(+1)이며 1차원 배열로 생성
    visited = [False]*BOARD                                 # 방문 처리

    ladder, snake = dict(), dict()

    for _ in range(n):                                 # 사다리 (小 -> 大)
        start, destination = map(int, input().split())
        ladder[start] = destination
    for _ in range(m):                                  # 뱀 (大 -> 小)
        start, destination = map(int, input().split())
        snake[start] = destination
    print(solution(1))