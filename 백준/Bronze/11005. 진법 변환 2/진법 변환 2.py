N, B = map(int, input().split())
ans = ""
while N != 0:
    remainder = N % B
    if remainder >= 10:
        ans += chr(remainder + 55)
    else:
        ans += str(remainder)
    N //= B
print(ans[::-1])