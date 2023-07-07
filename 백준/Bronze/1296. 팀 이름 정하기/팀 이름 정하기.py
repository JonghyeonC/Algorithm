name = input()
namelist = []
check = []
c = []
for i in range(int(input())):
    name1 = input()
    name2 = name1+name
    L = name2.count('L')
    O = name2.count('O')
    V = name2.count('V')
    E = name2.count('E')
    namelist.append(name1)
    check.append(((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100)
for i in range(len(check)):
    if check[i] == max(check):
        c.append(namelist[i])
c.sort()
print(c[0])