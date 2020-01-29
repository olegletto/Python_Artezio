a = int(input('Введите число А '))
b = int(input('Введите число B '))
c = int(input('Введите число C '))

x = 0
for i in range(a, b):
    if i % c == 0:
        x += 1
       
print ('Всего в интервале ' + str(x) + ' чисел делятся на ' + str(c))