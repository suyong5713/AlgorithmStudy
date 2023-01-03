def solution(n, results):
    answer = 0
    # 인덱스번째 사람을 이긴 사람
    win = [set([]) for _ in range(n+1)]
    # 인덱스번째 사람에게 진 사람
    lose = [set([]) for _ in range(n+1)]
    for winner, loser in results:
        # loser를 이긴사람 그래프에 winner 추가
        win[loser].add(winner)
        # winner에게 진사람 그래프에 loser 추가
        lose[winner].add(loser)
    for i in range(1, n + 1):
        # i번 선수를 이긴 사람(winner)은 i번 선수에게 진 선수에게도 반드시 이김
        for winner in win[i]:
            lose[winner].update(lose[i])
        # i번 선수에게 진 사람(loser)은 i번 선수를 이긴 선수에게도 반드시 짐
        for loser in lose[i]:
            win[loser].update(win[i])
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer