# https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 프로그래머스, 멀쩡한 사각형 (Level. 2)

def solution(w, h):
    a = w
    b = h
    
    # w와 h에 대해 직사각형의 대각선을 그릴 때 꼭지점이 정확히 일치하는 부분 = 최대공약수의 배수
    while b > 0:
        a, b = b, a % b
        
    # 온전한 사각형의 개수 = 전체 사각형 개수 - (최대공약수 * 갈라진 사각형의 개수)
    return w * h - (w + h - a)
