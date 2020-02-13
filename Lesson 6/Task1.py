class EvenIterator:
    def __iter__(self):
        return self


    def __init__(self, lst):
        self.lst = lst
        self.item = 0
        self.len = len(lst)


    def __next__(self):
        if self.item < self.len:
            element = self.lst[self.item]
            self.item += 2
            return element
        else:
            raise StopIteration


iter = EvenIterator([11,12,13,14,15,16,17,18,19,20])
for i in iter:
    print(i)

