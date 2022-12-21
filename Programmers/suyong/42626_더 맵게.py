from heapq import *
def solution(scoville, K):
    heapify(scoville)
    mix_count = 0
    while(scoville[0] < K and len(scoville) > 1):
        food1 = heappop(scoville)
        food2 = heappop(scoville)
        mix_value = food1 + food2 * 2
        heappush(scoville, mix_value)
        mix_count += 1
    if scoville[0] > K:
        return mix_count
    else: return -1