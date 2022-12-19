def solution(number, k):
    answer = ''

    t_len = len(number) - k
    r_len = len(number) - t_len

    while t_len > 0:
        front = number[:r_len + 1]

        max_num = max_idx = -1
        for idx, num in enumerate(front):
            if max_num < int(num):
                max_num = int(num)
                max_idx = idx
            if max_num == 9:
                break

        answer += str(max_num)
        number = number[max_idx + 1:]
        t_len -= 1
        r_len = len(number) - t_len

    return answer

print(solution("1924", 2))