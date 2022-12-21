from heapq import *
def solution(operations):
    min_heap, max_heap = [], []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heappush(min_heap, num)
            heappush(max_heap, (-num, num))
        elif command == 'D':
            if min_heap:
                if num == 1:
                    max_val = heappop(max_heap)[1]
                    min_heap.remove(max_val)
                else:
                    min_val = min_heap.pop(0)
                    max_heap.remove((-min_val, min_val))
    return [max_heap[0][1], min_heap[0]] if min_heap else [0,0]