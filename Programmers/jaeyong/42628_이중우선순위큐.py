# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 이중우선순위큐 (Level. 3 / Heap)
# 풀이시간 : 20분

import heapq

def solution(operations):
    answer = []
    heapq.heapify(answer)
    
    for o in operations:
        op, num = o.split(" ")
        if op == 'I': heapq.heappush(answer, int(num))
        if op == 'D':
            if num == '1' and len(answer) > 0:
                answer.pop(answer.index(max(answer)))
            if num == '-1':
                heapq.heappop(answer)

    if len(answer) == 0: return [0, 0]
    return [max(answer), min(answer)]

# ============================================================= #

def main(t, operations, result):
    r = solution(operations)
    print('#{}: {}, {}, {}'.format(t + 1, result == r, result, r))

if __name__ == '__main__':
    operations = [
        ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], 
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    ]
    result = [
        [0, 0], 
        [333, -45]
    ]

    for t in range(2):
        main(t, operations[t], result[t])
