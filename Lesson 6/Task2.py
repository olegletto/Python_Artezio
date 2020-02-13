def attr_list(object):
    list_attr = [i for i in dir(object) if not i.startswith("_")]
    return list_attr


print(attr_list(5))
print(attr_list('hello'))