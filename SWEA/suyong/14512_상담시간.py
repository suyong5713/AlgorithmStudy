from itertools import permutations
for tc in range(int(input())):
    N, M = map(int,input().split())
    input_list = [list(map(int,input().split())) for _ in range(N)]
    # 상담원 번호를 순열로 세움
    perm = list(map(list, permutations(range(N))))
    result = float('inf')
    for test in perm:
        # 순열로 세운 한 경우에서 첫번째 상담원의 상담 가능 시간을 추출
        min_start, max_start = input_list[test[0]]
        # 모든 상담원이 가능한지 체크
        for p in range(min_start, max_start + 1):
            next_p = p + 1
            for idx, next_job in enumerate(test[1:]):
                min_start2, max_start2 = input_list[next_job]
                # 다음 상담원도 가능하면 1 더해서 그 다음 상담원 체크
                if min_start2 <= next_p <= max_start2:
                    next_p += 1
                else:
                    break
            # 처음 시작시간에서 상담원의 수 만큼 시간이 커졌으면 성공
            if next_p == p + len(test):
                # 최소 값 갱신.
                result = min(p, result)
    if result == float('inf'):
        print("#{} -1".format(tc + 1))
    else:
        print("#{} {}".format(tc + 1, result))