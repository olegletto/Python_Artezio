
c = 0
for i in range(0, 10):
    if i % 2 != 0:
        print(i * 2)
        c += 1
       
print ('Всего в интервале ' + str(c) + ' нечётных чисел')