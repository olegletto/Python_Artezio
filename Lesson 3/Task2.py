from functools import reduce
def foo(*args, **kwargs):
    s = []
    for i in args:
        s.append(i)
    for i in kwargs:
        s.extend(kwargs[i])


    def flatten(x):
        result = []
        for i in x:
            if hasattr(i, "__iter__") and not isinstance(i, int):
                result.extend(i)
            else:
                result.append(i)
        return result        


    s = flatten(s)
    s = flatten(s)        
        
    result_list = list(filter(lambda i: i != 0, s))
    mult = reduce(lambda x, y: x * y, result_list, 1)
    amount = reduce(lambda x, y: x + y, result_list, 0)
    
    return ['Произведение: ' + str(mult), 'Сумма: ' + str(amount)]


print(foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))