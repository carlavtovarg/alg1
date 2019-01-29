import random


class Calculator:
    def __init__(self, list):
        self.list = list
        self.__av = 0
        self.__min =0
        self.__max = 0
        print(self.list)

    def get_average(self):
        sum = 0
        for x in self.list:
            sum += x
        cant = len(self.list)
        self.__av = sum/cant
        return self.__av

    def get_maxim(self):
        self.__max = self.list[0]
        for x in self.list:
            if x > self.__max:
                self.__max = x
        return self.__max

    def get_minim(self):
        suma = 0
        cont = 0
        self.__min = self.list[0]
        for x in self.list:
            suma = suma + x
            cont += 1
            if x < self.__min:
                self.__min = x
        return  self.__min

    def clear(self):
        self.list.clear()

    def generate_random_list(self, x, y, z):
        for a in range(0, x):
            valor = random.randint(y, z)
            self.list.append(valor)
            print("the value in the position {0} is: {1}".format(a, valor))


lis1 = Calculator([2, 3, 4, 5])
print(str(lis1.get_average()))
print(str(lis1.get_maxim()))
print(str(lis1.get_minim()))
lis1.clear()
lis1.generate_random_list(3, 1, 10)
print(lis1.get_average())