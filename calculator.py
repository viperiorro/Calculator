# implement calculator

class Calculator:
    def __init__(self):
        self.__result = 0

    @property
    def result(self):
        return self.__result

    def add(self, num):
        self.__result += num
        return self

    def sub(self, num):
        self.__result -= num
        return self

    def mul(self, num):
        self.__result *= num
        return self

    def div(self, num):
        self.__result /= num
        return self

    def mod(self, num):
        self.__result %= num
        return self

    def clear(self):
        self.__result = 0
        return self

    def __str__(self):
        return str(self.__result)


if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(10).sub(5).mul(2).div(3).mod(2).result)
    print(calc.clear().result)
    print(calc.add(10).result)
    print(calc.sub(5).result)
    print(calc.mul(2).result)
    print(calc.div(3).result)
    print(calc.mod(2).result)
    print(calc.clear().result)
    print(calc.add(10).sub(5).mul(2).div(3).mod(2))