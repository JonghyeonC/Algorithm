N = int(input())
for _ in range(N):
    a, b = input().split()
    num = int(a)
    word_list = list(b)
    for word in word_list:
        print(word*num, end="")
    print()