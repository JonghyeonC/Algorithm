hour, minute = map(int, input().split())
time = int(input())

time_h = time // 60
time_m = time % 60

hour += time_h
minute += time_m

if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(hour, minute)