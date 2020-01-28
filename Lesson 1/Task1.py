s = input('Введите имя и фамилию')
while len(s) < 1 or len(s) > 1000:
        print('Попробуйте еще раз!')
        s = input('Введите имя и фамилию')
       
print (s.title())