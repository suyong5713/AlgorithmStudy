N, S = list(map(int, input().split()))
numbers = list(map(int,input().split()))
end, sub_sum = 0, 0
min_length = float('inf')
for start in range(len(numbers)):
    while sub_sum < S and end < len(numbers):
        sub_sum += numbers[end]
        end += 1
    if sub_sum >= S:
        min_length = min(min_length, end - start)
    sub_sum -= numbers[start]
if min_length == float('inf'):
    print(0)
else: print(min_length)
