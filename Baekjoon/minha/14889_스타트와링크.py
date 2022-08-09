from itertools import combinations

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

members = [i for i in range(N)]
startTeam = []
res = 9999999

for i in list(combinations(members, N//2)):
    startTeam.append(list(i))

for i in startTeam:
    linkTeam = list(set(members) - set(i))

    startComb = list(combinations(i, 2))
    startScore = 0
    for f, s in startComb:
        startScore += (ability[f][s] + ability[s][f])

    linkComb = list(combinations(linkTeam, 2))
    linkScore = 0
    for f, s in linkComb:
        linkScore += (ability[f][s] + ability[s][f])

    res = min(res, abs(startScore - linkScore))

print(res)