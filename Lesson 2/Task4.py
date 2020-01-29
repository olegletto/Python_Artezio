a = int(input('Введите начало: '))
b = int(input('Введите конец: '))
c = int(input('Введите шаг: '))
l = []
if c > 0:
    while a < b:
        l.append(a)
        a += c
else:
    while a > b:
        l.append(a)
        a += c
print (l)






