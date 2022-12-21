def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = []

    while routes:
        camera.append(routes.pop(0)[1])

        remove_cnt = 0
        for idx in range(len(routes)):
            idx -= remove_cnt

            if routes[idx][0] <= camera[-1] <= routes[idx][1]:
                routes.pop(idx)
                remove_cnt += 1

    return len(camera)