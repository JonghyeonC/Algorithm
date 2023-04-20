X = int(input())
stick = [64]
while sum(stick) > X:
    temp = stick.pop() // 2
    stick.extend([temp, temp])
    if sum(stick[:-1]) >= X:
        stick.pop()
print(len(stick))