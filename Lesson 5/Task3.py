class Observable(object):


    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def __repr__(self):
        kwargs = (', '.join(f"{key}={repr(value)}" for (key, value) in self.__dict__.items() if not key.startswith('_')))
        return f"{self.__class__.__name__}({kwargs})"
        

class X(Observable):
    pass



x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(x)
print(x.foo) #1
print(x.name) #'Amok'
print(x._bazz) #12
