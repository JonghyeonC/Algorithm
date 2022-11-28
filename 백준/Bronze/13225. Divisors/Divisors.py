N = int(input())
for _ in range(N):
    num = int(input())
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(f'{num} {len(divisors)}')