# 정렬 연산 시 0을 무시하기 위해 사용하는 메소드, arr에서 모든 0을 지우고 리턴한다
def remove_zero(arr):
    remove_cnt = 0

    for i in range(len(arr)):
        i -= remove_cnt
        if arr[i] == 0:
            arr.remove(arr[i])
            remove_cnt += 1

    return arr


def two_dimension_sort(arr, cal):
    new_arr = []
    res_arr = []

    # 이차원 리스트 arr에서 리스트 하나씩 0을 제거하고, 갯수를 카운트 해서 정렬 후 새로운 리스트에 넣는 과정
    for sa in arr:
        tmp = []
        sa = remove_zero(sa)
        set_sa = list(set(sa))
        for s in set_sa:
            tmp.append([s, sa.count(s)])

        tmp.sort(key=lambda x: (x[1], x[0]))
        new_arr.append(sum(tmp, []))

    # 새로운 리스트에서 제일 긴 길이를 구하는 과정
    max_cnt = -1
    for na in new_arr:
        max_cnt = max(max_cnt, len(na))

    # 새로운 리스트에서 제일 긴 길이만큼 0을 채워주는 과정
    for na in new_arr:
        if len(na) < max_cnt:
            for _ in range(max_cnt - len(na)):
                na.append(0)
            res_arr.append(na)
        else:
            res_arr.append(na)

    # R연산이면 그대로 리턴, C연산이면 행과 열 전치 후 리턴
    if cal == "R":
        return res_arr
    else:
        return list(map(list, zip(*res_arr)))


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

while True:
    col_A = list(map(list, zip(*A)))

    # 100초 넘으면 -1 출력 후 종료
    if cnt > 100:
        print(-1)
        break
    else:
        # 현재 배열이 r, c 보다 큰 경우 종료 조건을 만족하면 시간 출력 후 종료
        if len(A) >= r and len(col_A) >= c:
            if A[r - 1][c - 1] == k:
                print(cnt)
                break
        # 행의 길이가 크거나 같으면 R연산 후 시간 1 증가
        if len(A) >= len(col_A):
            A = two_dimension_sort(A, "R")
            cnt += 1
        # 열의 길이가 크면 C연산 후 시간 1 증가
        else:
            A = two_dimension_sort(col_A, "C")
            cnt += 1