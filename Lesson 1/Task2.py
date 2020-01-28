s = input("Введите слово для подсчета частоты встречающихся букв")
d = {} 
for i in set(s): 
    b = s.count(i, 0, len(s)) 
    d[i] = b 
print (d)