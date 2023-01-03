import heapq


# 1. heapq 라이브러리 없이 리스트만 사용

def solution(operations):
    nums = []
    for ope in operations:
        command, value = ope.split()
        if command == 'I':
            nums.append(int(value))
        elif command == 'D' and nums:
            if int(value) < 0:
                nums.pop(nums.index(min(nums)))
            else:
                nums.pop(nums.index(max(nums)))
    if len(nums) == 0:
        return [0, 0]
    else:
        return [max(nums), min(nums)]

# 2. heapq 라이브러리 사용

def solution(operations):
    heap = []
    for ope in operations:
        command, value = ope.split()
        if command == "I":
            heapq.heappush(heap, int(value))
        elif heap:
            if value == "1":
                # nlargest를 통해 큰 순서대로 정렬해 준 후 맨 앞만 슬라이싱
                heap = heapq.nlargest(len(heap), heap)[1:]
                # 다시 heap 구조로 정렬
                heapq.heapify(heap)
            elif value == "-1":
                heapq.heappop(heap)
    # 힙에 숫자가 존재한다면
    if heap:
        min_val = heapq.heappop(heap)
        if heap:
            max_val = heapq.nlargest(1, heap)[0]
        else:
            max_val = min_val
    else:
        max_val, min_val = 0, 0
    return [max_val, min_val]