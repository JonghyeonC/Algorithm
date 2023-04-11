import sys
from math import factorial


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    result = factorial(b) // (factorial(a) * factorial(b - a))
    print(result)