N = int(input())

nume = 1
deno = 1

idx = 0
flag = 0
while idx + 1 != N:
    if nume == deno == 1:
        deno += 1
    else:
        if flag == 0:
            nume -= 1
            deno += 1
            if nume == 0 and deno == 3:
                nume += 1
                deno -= 1
                nume, deno = deno, nume
                flag = 1
            elif nume == 0:
                nume += 1
                flag = 1
        elif flag == 1:
            nume += 1
            deno -= 1
            if deno == 0:
                deno += 1
                flag = 0
    idx += 1
print(f'{nume}/{deno}')