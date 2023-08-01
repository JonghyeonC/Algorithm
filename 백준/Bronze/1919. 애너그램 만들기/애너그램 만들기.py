word_1 = list(input())
word_2 = list(input())
a = word_1[:]
b = word_2[:]
x = [i for i in word_1 if not i in b or b.remove(i)]
y = [j for j in word_2 if not j in a or a.remove(j)]
print(len(x) + len(y))