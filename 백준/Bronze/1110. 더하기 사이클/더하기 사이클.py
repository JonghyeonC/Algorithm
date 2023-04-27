N = int(input())
number = N
count = 0
while True:
  temp = N // 10
  units = N % 10
  N = (units * 10) + ((temp + units) % 10)
  count += 1
  if (N == number):
    break

print(count)