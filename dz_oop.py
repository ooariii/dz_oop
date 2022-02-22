# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
class Example:
    def __init__(self):
        self.h = 0
        self.d = 0
        self.g = 0
        self.gl = []
        self.sogl = []

    def func (self, a):
        if type(a) is str:
            for i in a:
                if i in 'aeoiu':
                    self.h += 1
                    self.gl.append(i)
                else:
                    self.d += 1
                    self.sogl.append(i)
            print('Количество гласных', self.h)
            print('Количество согласных', self.d)
            print('Длина слова:', self.func1(a))
            if (self.h * self.d) <= self.func1(a):
                print('Гласные:', self.gl)
            else:
                print('Согласные:', self.sogl)
        elif type(a) is int:
            for i in str(a):
                i = int(i)
                if (i % 2) == 0:
                    self.g += i
            print('Произведение: ', self.g * self.func1(a))

    def func1(self, a):
        return len(str(a))

example = Example()
b = input()
if b.isalpha():
    example.func(b)
elif b.isdigit():
    example.func(int(b))