import sys
mod_list = []
for i in range(0, 10):
    num = int(sys.stdin.readline().rstrip())
    mod = num % 42
    if (mod not in mod_list):
        mod_list.append(mod)
print(len(mod_list))