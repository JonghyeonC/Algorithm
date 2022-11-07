def solution(a, b, n):
    answer = 0
    while n >= a:
        change_num = n // a
        n = n - (change_num * a) + change_num * b
        answer += change_num * b
    return answer