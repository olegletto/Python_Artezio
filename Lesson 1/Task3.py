s = input('Введите строку')

if len(s) < 2:
    print('')
else:
    start = s[0:2]
    end = s[-2:]
    print (start + end)