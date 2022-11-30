from collections import deque

N = int(input())

A = deque()
B = deque()
C = deque()
D = deque()

car = []
for num in range(N):
    time, road = map(str, input().split())
    if road == 'A':
        A.append([num, int(time)])
    elif road == 'B':
        B.append([num, int(time)])
    elif road == 'C':
        C.append([num, int(time)])
    else:
        D.append([num, int(time)])

cur_time = 0
answer = [-1] * N
while A or B or C or D:
    min_time = int(1e9)
    A_waiting = B_waiting = C_waiting = D_waiting = False

    if A:
        A_min = A[0][1]
        min_time = min(min_time, A_min)
        if A_min <= cur_time:
            A_waiting = True
    if B:
        B_min = B[0][1]
        min_time = min(min_time, B_min)
        if B_min <= cur_time:
            B_waiting = True
    if C:
        C_min = C[0][1]
        min_time = min(min_time, C_min)
        if C_min <= cur_time:
            C_waiting = True
    if D:
        D_min = D[0][1]
        min_time = min(min_time, D_min)
        if D_min <= cur_time:
            D_waiting = True

    if A_waiting and B_waiting and C_waiting and D_waiting:
        break

    if not(A_waiting or B_waiting or C_waiting or D_waiting):
        cur_time = min_time
        continue

    if A_waiting and not D_waiting:
        idx, time = A.popleft()
        answer[idx] = cur_time

    if B_waiting and not A_waiting:
        idx, time = B.popleft()
        answer[idx] = cur_time

    if C_waiting and not B_waiting:
        idx, time = C.popleft()
        answer[idx] = cur_time

    if D_waiting and not C_waiting:
        idx, time = D.popleft()
        answer[idx] = cur_time

    cur_time += 1

for a in answer:
    print(a)