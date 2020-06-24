from math import sqrt


class Vector:
    def __init__(self, data):
        self.__data = data

    def __get__(self):
        return self.__data

    def __set__(self, val):
        if not str(val).isnumeric(): 
            raise Exception
        elif type(val) is list:
            self.__data = val
        elif type(val) is Vector:
            self = val
        else:
            raise Exception

    def __getitem__(self, key):
        return self.__data[key]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __str__(self):
        return 'vector: %s' % str(self.__data)

    def __len__(self):
        return len(self.__data)

    def __add__(self, other):
        if self.__isconformant(self, other):
            return Vector([self[i] + other[i] for i in range(len(self))])
        else:
            raise Exception

    def __sub__(self, other):
        if self.__isconformant(self, other):
            return Vector([self[i] - other[i] for i in range(len(self))])
        else:
            raise Exception

    def __mul__(self, other):
        if str(other).isnumeric():
            return Vector([val * other for val in self])
        elif self.__isconformant(self, other):
            return sum([self[i] * other[i] for i in range(len(self))])
        else:
            raise Exception

    def __eq__(self, other):
        if str(other).isnumeric():
            raise Exception
        elif self.__isconformant(self, other):
            return False not in set([
                self[i] == other[i] for i in range(len(self))
            ])
        else:
            return False

    def length(self):
        return sqrt(sum([val * val for val in self]))

    __isconformant = lambda self, x, y: True if len(x) == len(y) else False


if __name__ == '__main__':
    vect1 = Vector([1, 2, 3, 4])
    print('vect1: ', vect1)
    vect1[0] = 8
    print('changed vect1[0]: ', vect1[0])
    vect2 = Vector([1, 2])
    vect2 = [5, 6, 7, 8]
    vect2[3] = 9
    print('vect2: ', vect2)
    print('vect1 + vect2: ', vect1 + vect2)
    print('vect1 * vect2', vect1 * vect2)
    vect2 = vect1 * 3
    print(vect2, vect1, end=' ')
    print(vect1 == vect2)
