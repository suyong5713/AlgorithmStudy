from collections import deque
def solution(A, B):
    answer = 0
    A = deque(sorted(A))
    B = deque(sorted(B))
    while(B):
        current_B = B.popleft()
        if A[0] < current_B:
            A.popleft()
            answer += 1
    return answer