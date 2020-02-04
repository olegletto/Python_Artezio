# функция должна вернуть квадраты элементов коллекции
def function1(*a):
    return [i * 2 for i in a]


print(function1(1, 5, 7, 3))


# функция должна вернуть только элементы на четных позициях
def function2(*a):
    return [i for i in a if a.index(i) % 2 == 0]


print(function2(1, 5, 7, 3))


# функция возвращает кубы четных элементов на нечетных позициях
def function3(*a):
    return [i * 3 for i in a if a.index(i) % 2 != 0 & i % 2 == 0]


print(function3(1, 5, 7, 3))


# Со встроенными функциональными средствами

a = [1, 5, 7, 3]

d = list(map(lambda i: i * 2, a))
print(d)

d = list(filter(lambda i: a.index(i) % 2 == 0, a))
print(d)

d = list(map(lambda i: i * 3, filter(lambda i: a.index(i) % 2 != 0 & i % 2 == 0, a)))
print(d)
