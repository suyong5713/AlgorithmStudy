def solution(number, k):
    global arr, l, res

    arr = list(map(int, list(number)))
    # 주어진 number 길이
    l = len(arr)
    # c는 선택된 숫자 개수, idx는 가장 최근에 선택된 숫자 인덱스 + 1
    c, idx = 0, 0
    # 정답
    res = 0

    # c가 l-k(다 빼고 남은 숫자 개수)보다 작을 때만 반복
    while c < l - k:
        # 최대값 초기화
        m = 0
        # idx부터 k+c+1까지 탐색
        # 규칙 찾아보니 현재 idx에서 k+c+1까지만 찾아야 온전한 숫자 도출 가능
        for i in range(idx, k + c + 1):

            # 9가 무조건 최대이므로 끝까지 찾지 않고 도중에 탈출
            # 이거 하니까 테스트 10 통과됨
            if arr[i] == 9:
                m = 9
                curr_idx = i
                break

            # 현재 위치가 더 크다면 최대값으로 최신화
            elif arr[i] > m:
                m = arr[i]
                curr_idx = i

        # 자리올림 후 더함
        res = res * 10 + m
        # idx 갱신
        idx = curr_idx + 1
        # 선택된 숫자 개수 갱신
        c += 1

    return str(res)