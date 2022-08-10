#import sys
#sys.stdin = open('1959.txt')

num = int(input())

for tc in range(1, num + 1):
    a, b = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    answer = 0
    if a < b:
        for i in range(b - a + 1):
            total = 0
            for j in range(a):
                total += ai[j] * bi[j+i]
            if answer < total:
                answer = total

    if a > b:
        for i in range(a - b + 1):
            total = 0
            for j in range(b):
                total += ai[j+i] * bi[j]
            if answer < total:
                answer = total

    print(f'#{tc} {answer}')
