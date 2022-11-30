def power(num, n):
    if n == 0:
        return 1
    if n == 1:
        return num % c
    x = power(num, n // 2)
    if n % 2 == 0:
        return (x * x) % c
    else:
        return (x * x * a) % c


a, b, c = map(int, input().split())
result = power(a, b)
print(result)