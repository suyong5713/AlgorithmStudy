import sys
sys.stdin = open("input.txt", "r")

def sorting(arr):
    row_size = 0
    # 한 행씩 정렬
    for index in range(len(arr)):
        # 등장 횟수를 저장하기 위한 딕셔너리 (key : number, value : 등장 횟수)
        num_dict = {}
        # 새 배열에 저장
        new_arr = []
        for r in arr[index]:
            # 숫자가 0이면 넘어감
            if r == 0:
                continue
            # 딕셔너리 key에 해당 숫자가 있으면 값 1 증가
            elif r in num_dict:
                num_dict[r] += 1
            # 딕셔너리에 없으면 값 1로 초기화
            else:
                num_dict[r] = 1
        # value(등장 횟수), key(숫자)를 기준으로 정렬
        sorted_arr = sorted(num_dict.items(), key=lambda x: (x[1], x[0]))
        for s in sorted_arr:
            new_arr.append(s[0])
            new_arr.append(s[1])
        # 다시 arr에 한 행씩 넣어줌
        arr[index] = new_arr[:]
        # 모든 행 중 최대 길이
        row_size = max(row_size, len(arr[index]))
    # 제일 긴 행 길이에 맞춰 나머지 행에 0을 추가해줌
    for a in arr:
        for _ in range(row_size - len(a)):
            a.append(0)


r, c, k = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(3)]
time = 0
while True:
    if len(nums) > r - 1 and len(nums[0]) > c - 1:
        if nums[r - 1][c - 1] == k:
            break
    # 100초가 지나면 -1 출력
    if time > 100:
        time = -1
        break
    # 행 개수 >= 열 개수 => 행 정렬
    if len(nums) >= len(nums[0]):
        sorting(nums)
    # 열 개수 > 행 개수 => 열 정렬
    elif len(nums) < len(nums[0]):
        nums = list(map(list, zip(*nums)))
        sorting(nums)
        nums = list(map(list, zip(*nums)))
    time += 1
print(time)
