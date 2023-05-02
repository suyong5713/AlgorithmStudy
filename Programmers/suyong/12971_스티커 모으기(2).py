def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]

    dp2[1] = sticker[1]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    return max(dp1[len(sticker) - 2], dp2[len(sticker) - 1])
