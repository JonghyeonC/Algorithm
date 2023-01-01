N = int(input())
cnt = 0
number = 1
while True:
    if '666' in str(number):
        cnt += 1
    if cnt == N:
        print(number)
        break
    number += 1