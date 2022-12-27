def solution(n, times):
    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += mid // time

        if n <= cnt:
            right = mid
        else:
            left = mid + 1

    return left