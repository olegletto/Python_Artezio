def chain(value):
    for el in value:
        for i in el:
            yield i

