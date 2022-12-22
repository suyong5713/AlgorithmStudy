import heapq


def solution(operations):
    # 힙 리스트
    heap = []

    # 주어진 연산에 대해
    for op in operations:
        # 시행 연산과 숫자를 나누어줌
        work, num = op.split()
        num = int(num)

        # 삭제 연산 시
        if work == "D":
            # 힙이 비어있지 않을 때
            if heap:
                # 숫자가 1이라면
                if num > 0:
                    # 힙에서 최대값 삭제
                    heap.remove(max(heap))
                # 숫자가 -1이라면
                else:
                    # 힙에서 최소값 삭제
                    heapq.heappop(heap)
        # 추가 연산 시
        else:
            # 힙에 새로운 숫자 추가
            heapq.heappush(heap, num)

    # 힙이 비어있을 경우
    if len(heap) == 0: return [0, 0]

    return [max(heap), heap[0]]