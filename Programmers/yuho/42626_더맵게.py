import heapq


def solution(scoville, K):
    # 섞은 횟수
    cnt = 0
    # 모든 원소가 K이상인지 확인
    flag = False
    # scoville 리스트를 힙으로 만들어줌
    heapq.heapify(scoville)

    # 힙 원소가 2개 이상일 때만 반복
    while len(scoville) > 1:
        # 섞은 횟수 1 증가
        cnt += 1
        # 스코빌이 가장 작은 음식
        food1 = heapq.heappop(scoville)
        # 스코빌이 두번째로 작은 음식
        food2 = heapq.heappop(scoville)
        # 섞어서 새로운 음식 -> f1 + f2 * 2
        new_food = food1 + food2 * 2
        # 기존 힙에 섞은 음식 추가
        heapq.heappush(scoville, new_food)

        # 모든 스코빌 원소가 K이상일 때만
        # flag를 True로 바꾼 뒤 반복문 탈출
        for food in scoville:
            if food < K:
                break
        else:
            flag = True
            break

    # 모든 원소 K 이상 만들지 못할 시 -1 반환
    if not flag: return -1
    return cnt