def solution(routes):
    routes = sorted(routes, key=lambda route: route[1])
    camera = -30001
    answer = 0
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer