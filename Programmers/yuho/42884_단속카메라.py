def solution(routes):
    answer = 0
    # cctv 초기 위치
    cctv = -30000
    # 나간 지점이 작은 순으로 정렬
    routes.sort(key=lambda arr: arr[1])

    # 정렬된 루트 리스트 전체에 대해
    for route in routes:
        # 현재 cctv 위치가 route 시작지점보다 작을 시
        if cctv < route[0]:
            # cctv 하나 설치
            answer += 1
            # route 나간 지점을 cctv 위치로 설정
            # 나간 지점을 기준으로 정렬했기에 얘랑 겹치는 cctv는 시작지점이 얘보다 작을 수밖에 없음
            cctv = route[1]

    return answer