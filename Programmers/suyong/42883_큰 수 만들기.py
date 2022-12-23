def solution(number, k):
    number = list(number)
    # 첫번째 수 저장
    result = [number.pop(0)]
    for n in number:
        # 가장 마지막 수와 현재 수를 비교하여
        if result[-1] < n:
            # 현재 수가 더 크다면 기존 수를 제거하고 현재 수로 교체.
            while result and result[-1] < n and k > 0:
                k -= 1
                result.pop()
            result.append(n)
        # 현재 수보다 기존의 수가 더 크다면 수를 제거하지 않음
        # 제거할 수 있는 기회(k)가 0이면 제거하지 못함.
        elif result[-1] >= n or k == 0:
            result.append(n)
    # 위 과정을 전부 진행 하고도 k가 남아 있다면, 만들어진 숫자열의 마지막 k 자리를 제거
    for _ in range(k):
        result.pop()
    answer = ''.join(result)
    print(answer)
    return answer