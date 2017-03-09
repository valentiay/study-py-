import sys


class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.r = real
        self.i = imaginary

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return ComplexNumber(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        return ComplexNumber(self.r * other.r - self.i * other.i,
                             self.r * other.i + self.i * other.r)

    def __div__(self, other):
        return ComplexNumber((self.r * other.r + self.i * other.i) /
                             (other.r ** 2 + other.i ** 2),
                             (other.r * self.i - other.i * self.r) /
                             (other.r ** 2 + other.i ** 2))

    def __str__(self):
        s = ''
        if self.r != 0:
            s = str('%.2f' % round(self.r, 2))
            if self.i > 0:
                s += ' + '
        if self.i < 0:
            s += ' - '
        if self.i != 0:
            if self.r == 0 and self.i < 0:
                s = '-'
            s = s + str('%.2f' % round(abs(self.i), 2)) + 'i'
        if self.r == 0 and self.i == 0:
            s = '0.00'
        return s


if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print eval(line.strip())
