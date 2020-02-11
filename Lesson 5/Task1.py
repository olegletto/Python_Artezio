from math import sqrt

class Complex(object):

    def __init__(self, a):
        self.real = float(a[0])
        self.imag = float(a[1])


    def __str__(self):
        if self.imag >= 0:
            return "{:.2f}+{:.2f}i".format(self.real, self.imag)
        return "{:.2f}{:.2f}i".format(self.real, self.imag)


    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex([real, imag])


    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex([real, imag])


    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + other.real * self.imag
        return Complex([real, imag])


    def __truediv__(self, other):
        real = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
        imag = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
        return Complex([real, imag])


    def __abs__(self):
        real = sqrt(self.real ** 2 + self.imag ** 2)
        return Complex([real, 0])


C = Complex("2 1".split())
D = Complex("5 6".split())
print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(abs(C))
print(abs(D))
