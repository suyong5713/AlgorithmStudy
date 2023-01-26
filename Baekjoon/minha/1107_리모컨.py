N = int(input())
M = int(input())
answer = abs(N - 100)

if M != 0:
    broken = list(input().split())

    for target in range(1_000_000):
        flag = True
        for t in str(target):
            if t in broken:
                flag = False
                break

        if flag:
            answer = min(answer, abs(N - target) + len(str(target)))

        # for target in range(1_000_000):
        #     for t in str(target):
        #         if t in broken:
        #             break
        #     else:
        #         answer = min(answer, abs(N - target) + len(str(target)))

    print(answer)

else:
    print(min(answer, len(str(N))))