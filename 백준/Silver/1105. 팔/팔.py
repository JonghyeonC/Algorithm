L, R = input().split()
ans = 0
if len(L) != len(R):
    ans = 0
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == "8":
                ans += 1
        elif L[i] != R[i]:
            break
print(ans)