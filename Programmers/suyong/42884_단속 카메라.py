def solution(routes):
    # 진출 지점 기준으로 정렬
    routes.sort(key = lambda x: x[1])
    # 입력제한 최솟값 -30000
    camera = -30001
    answer = 0
    for route in routes:
        # 진입 지점 전에 카메라가 위치하면 관측 불가
        if camera < route[0]:
            camera = route[1]
            answer += 1
    return answer