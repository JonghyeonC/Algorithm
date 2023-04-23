from math import factorial


N, M = map(int, input().split())
numerator = factorial(N)
denominator = factorial(N - M) * factorial(M)
print(numerator // denominator)