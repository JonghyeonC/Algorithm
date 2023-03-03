s = input()
r = ""
for i in s:
    if i.isupper():
        r += i.lower()
    else:
        r += i.upper()
print(r)
