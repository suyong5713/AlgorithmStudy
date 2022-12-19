import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    flag = True

    while flag:
        if len(scoville) == 1:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first + second * 2)
        answer += 1

        if scoville[0] >= K:
            flag = False

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))