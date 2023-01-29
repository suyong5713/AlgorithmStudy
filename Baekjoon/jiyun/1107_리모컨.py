
def solution() -> int:
    ans = abs(n - 100)
    for i in range(1000001):
        numArr = list(str(i))
        flag = False
        for k in numArr:            # 숫자를 누를 수 있는 지 체크
            if int(k) in arr:
                flag = True
                break

        if flag: continue
        else:                       # 숫자를 누를 수 있는 경우 : n까지 가는 거 & 숫자를 누른 횟수를 비교
            ans = min(ans, abs(n - i) + len(str(i)))
    return ans


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    if m != 0: arr = list(map(int, input().split()))
    else: arr = []
    print(solution())