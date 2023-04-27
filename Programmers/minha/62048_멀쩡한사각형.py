def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    square = w * h
    gcd = get_gcd(w, h)

    return square - (w + h - gcd)

print(solution(8, 12))