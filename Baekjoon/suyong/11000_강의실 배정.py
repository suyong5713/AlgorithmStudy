import heapq


N = int(input())

lecture_list = [list(map(int, input().split())) for _ in range(N)]

lecture_list.sort()
#우선순위 큐: 큐에 저장되는 값들이 항상 정렬상태를 유지.
lecture_queue = []
heapq.heappush(lecture_queue, lecture_list[0][1])
#두번째 강의부터 마지막 강의까지 체크
for i in range(1, N):
    print(lecture_queue)
    #현재 강의의 시작 시각이 이전 강의의 종료 시각보다 이르다면 강의실 개설
    if lecture_list[i][0] < lecture_queue[0]:
        heapq.heappush(lecture_queue, lecture_list[i][1])
    #현재 강의의 시작 시각이 이전 강의의 종료 시각보다 같거나 늦다면 강의실 개설 안함.
    else:
        #이전 강의를 우선순위 큐에서 제거. 이후 현재 강의를 추가.
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, lecture_list[i][1])
#우선순위 큐에 남아있는 강의 수 만큼 강의실 필요.
print(len(lecture_queue))