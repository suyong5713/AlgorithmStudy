def solution(n, times):
    # 최소 심사 시간 ~ 최대 심사 시간을 left, right로 지정하고 이분탐색
    left, right = min(times), max(times) * n
    while left < right:
        mid = (left + right)//2
        # mid 시간 내에 심사 가능한 사람 수
        available = 0
        for time in times:
            # 각각의 심사관들의 mid시간 내에 심사 가능한 사람 수 만큼 증가
            available += mid // time
        if available >= n:
            # 처리해야할 사람보다 처리가능한 사람 수가 많으면
            # right 값을 감소 시켜서 더 낮은 범위 탐색
            right = mid
        else:
            # 처리해야할 사람보다 처리 가능한 사람 수가 적으면
            # left 값을 증가 시켜서 더 높은 범위 탐색
            left = mid + 1
    answer = left
    return answer