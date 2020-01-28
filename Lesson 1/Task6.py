i = input('Введите число')
i = int(i)
d = {a: a ** 2 for a in range(i+1)}
d.pop(0)
print (d)