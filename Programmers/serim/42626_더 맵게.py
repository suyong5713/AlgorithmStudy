import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        # 가장 작은 수
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer
        else:
            # 두번째로 작은 수
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
            answer += 1
    if scoville[0] > K:
        return answer
    else:
        return -1