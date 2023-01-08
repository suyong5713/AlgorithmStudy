# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게 (Level. 2 / Heap)
# 풀이시간 : 15분

# [섞은 음식의 스코빌 지수]
# 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq

def solution(scoville, K):
    answer = 0

    heap = scoville[:]
    heapq.heapify(heap)

    while len(heap) >= 2:
        if heap[0] >= K: break  # 최소값이 K 이상이면 모든값이 K 이상
        if len(heap) < 2: break # 2개 미만으로 있는 경우 더 이상 계산불가

        min_scoville = heapq.heappop(heap)
        sec_scoville = heapq.heappop(heap)

        mix_scoville = min_scoville + (2 * sec_scoville)

        heapq.heappush(heap, mix_scoville)
        answer += 1

    if heap[0] < K: return -1
    return answer

# ============================================================= #

def main(t, scoville, K, result):
    r = solution(scoville, K)
    print('#{}: {}, {}, {}'.format(t + 1, result == r, result, r))

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    result = 2

    main(0, scoville, K, result)
