import heapq

def solution(operations):
    my_heap = []

    for op in operations:
        o = op[0]
        num = int(op[2:])

        if o == "I":
            heapq.heappush(my_heap, num)
        elif o == "D":
            if len(my_heap) == 0:
                continue
            else:
                if num == -1:
                    heapq.heappop(my_heap)
                else:
                    my_heap = heapq.nlargest(len(my_heap), my_heap)[1:]
                    heapq.heapify(my_heap)

    if my_heap:
        max_val = heapq.nlargest(1, my_heap)[-1]
        min_val = heapq.heappop(my_heap)
        return [max_val, min_val]
    else:
        return [0, 0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))