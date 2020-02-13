def cycle(value):
    result = []
    for i in value:
        result.append(i)
        yield i
        
        
    while result:
        for i in result:
            yield i 

