def dictionary(key, value):
    if len(value) >= len(key):
        result = dict(zip(key, value))
    else:
        result = dict(zip(key, value + [None] * (len(key) - len(value))))
    
    return result


print(dictionary(['a','b','c','d','e'],[1,2,3,4,5,6,7]))
print(dictionary(['a','b','c','d','e'],[1,2,3]))